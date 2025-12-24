#util
class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(request.__dir__())
        print(1111111111111111)
        print(request.POST)
        print(request.FILES)
        print(22222222222222)
        response = self.get_response(request)
       

        return response