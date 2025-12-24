import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
import hashlib
import base64

NULL = {"null": True, "blank": True}


class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.localtime, editable=False)
    updated_at = models.DateTimeField(**NULL)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name="%(app_label)s_%(model_name)s_created_by",
        editable=False,
        **NULL,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name="%(app_label)s_%(model_name)s_updated_by",
        **NULL,
    )

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = timezone.localtime()

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class ChoiceModelMixin(BaseModelMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(**NULL)

    class Meta:
        abstract = True


class ShortUUIDField(models.CharField):
    description = "A short UUID field for generating unique IDs"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 12
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_id():
        """
        Generates a unique 12-character ID using a random UUID.
        """
        random_uuid = uuid.uuid4().hex
        to_hash = f"{settings.SECRET_KEY}{random_uuid}"
        hash_object = hashlib.sha256(to_hash.encode())
        hash_digest = hash_object.digest()

        # Get a base64-encoded string, then trim to 12 characters
        encoded = base64.urlsafe_b64encode(hash_digest).rstrip(b"=")
        return encoded[:12].decode("utf-8")
    
    @staticmethod
    def set_unique_ids(apps, model_name, app_name, field_name, batch_size=100):
        Model = apps.get_model(app_name, model_name)
        objects = Model.objects.all()
        total_objects = objects.count()
        print(f"Starting to update {field_name} for {total_objects} {model_name}s.")

        for start in range(0, total_objects, batch_size):
            end = min(start + batch_size, total_objects)
            print(f"Processing {model_name}s {start} to {end - 1}.")

            to_update = []
            for obj in objects[start:end]:
                setattr(obj, field_name, ShortUUIDField.generate_id())
                to_update.append(obj)

            Model.objects.bulk_update(to_update, [field_name])
            
            print(f"Updated {field_name} for {model_name}s {start} to {end - 1}.")

        print(f"Completed updating {field_name} for all {model_name}s.")

    def pre_save(self, model_instance, add):
        """
        Overrides the pre_save method to assign a unique ID to the field before saving.
        """
        if add and not getattr(model_instance, self.attname):
            # Try generating a unique ID and save.
            max_retries = 10
            for attempt in range(max_retries):
                value = ShortUUIDField.generate_id()
                if not model_instance.__class__._default_manager.filter(**{self.attname: value}).exists():
                    setattr(model_instance, self.attname, value)
                    return value
            raise ValueError("Unable to generate a unique ID after multiple attempts")
        return super().pre_save(model_instance, add)

    def get_prep_value(self, value):
        """
        Prepares the value for the database. Generates a new ID if the value is None.
        """
        if value is None:
            value = self.pre_save(self.model_instance, add=True)
        return value
