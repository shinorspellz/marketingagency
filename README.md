# Marketing Agency - One Day Agency Clone

A Next.js and Tailwind CSS clone of the One Day Agency website.

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn install
# or
pnpm install
```

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Features

- Modern Next.js 14 with App Router
- Tailwind CSS for styling with custom color accents
- Video background support in Hero section
- Responsive design
- Mobile-friendly navigation
- Color accents throughout (Orange, Blue, Green, Purple, Yellow)
- Logo support with fallback to text
- All major sections from the original website:
  - Hero section with video background
  - Services showcase with color accents
  - Clients grid with logo support
  - Testimonials with quote styling
  - Case studies with hover effects
  - Latest news with category colors
  - FAQ section with accordion
  - Call-to-action with gradient accents
  - Comprehensive footer with color accents

## Setup Instructions

### Adding Video Files

To enable the video background in the Hero section, add your video files to the `public` directory:

- `public/hero-video.mp4` - Main video file (MP4 format)
- `public/hero-video.webm` - Fallback video file (WebM format, optional)
- `public/hero-poster.jpg` - Poster image shown before video loads

If video files are not available, the Hero section will display a gradient fallback.

### Adding Logo Files

1. **Main Logo**: Add `public/logo.svg` or `public/logo.png` for the navigation bar
   - If not provided, the site will fallback to text "One Day Agency"

2. **Client Logos**: Add client logos to `public/clients/` directory:
   - Format: SVG or PNG files
   - Naming: Use lowercase with hyphens (e.g., `unidays.svg`, `netflix.svg`)
   - If logos are missing, client names will display as text

3. **Case Study Images**: Add case study images to `public/case-studies/`:
   - `tourism.jpg`
   - `motorsports.jpg`
   - `fmcg.jpg`
   - If images are missing, gradient placeholders will be shown

## Project Structure

```
├── app/
│   ├── layout.tsx      # Root layout with Navbar and Footer
│   ├── page.tsx        # Home page
│   └── globals.css     # Global styles with Tailwind
├── components/
│   ├── Navbar.tsx      # Navigation component
│   ├── Hero.tsx        # Hero section
│   ├── Services.tsx    # Services showcase
│   ├── Clients.tsx     # Clients grid
│   ├── Testimonials.tsx # Client testimonials
│   ├── CaseStudies.tsx # Case studies section
│   ├── LatestNews.tsx  # News section
│   ├── FAQ.tsx         # FAQ accordion
│   ├── CTA.tsx         # Call-to-action
│   └── Footer.tsx      # Footer component
└── public/             # Static assets
```

## Build

To create a production build:

```bash
npm run build
npm start
```

## Technologies

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS framework

