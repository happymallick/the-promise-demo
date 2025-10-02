"""
Single-file Flask app: The Promise - Landing page for full e-commerce site (services & products)

How to run:
 1. pip install flask
 2. python the_promise_landing.py
 3. Open http://127.0.0.1:5000 in your browser

This is a starter template. Replace product/service data and styles as needed.
"""
from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Sample data (replace with database/real content later)
PRODUCTS = [
    {"id": 1, "name": "Rechargeable Motion LED Light", "price": "₹499", "desc": "USB rechargeable night light for home and wardrobe."},
    {"id": 2, "name": "Mini Hand Wash Pump", "price": "₹799", "desc": "Compact automatic hand wash pump - hygienic & portable."},
    {"id": 3, "name": "Smart Electric Gauge", "price": "₹1,299", "desc": "Precision electric gauge for home and workshop."},
    {"id": 4, "name": "Home Cleaning Service (Monthly)", "price": "₹2,499", "desc": "Professional monthly cleaning by trained staff."},
]

SERVICES = [
    {"title": "Domestic Helpers", "short": "Maid, Cook, Caretaker", "long": "Trusted domestic manpower: trained, background-checked staff for home and office."},
    {"title": "CSC & Retail Support", "short": "Digital & CSC services", "long": "Point-of-service support for CSC operations, billing, and retail promotions."},
    {"title": "Sales & Placement", "short": "Hiring & Placement", "long": "End-to-end hiring and placement services for households and small businesses."},
]

TEMPLATE = r"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>The Promise — Products & Services</title>
    <!-- Tailwind CDN for quick styling (good for prototype). Replace with your own CSS in production. -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      /* small custom tweaks */
      .logo-mark { width: 48px; height: 48px; }
      .glass { background: rgba(255,255,255,0.6); backdrop-filter: blur(6px); }
    </style>
  </head>
  <body class="bg-gradient-to-b from-slate-50 to-slate-100 text-slate-800">
    <header class="shadow-sm sticky top-0 bg-white/60 glass z-50">
      <div class="mx-auto max-w-6xl px-6 py-4 flex items-center justify-between">
        <a href="#" class="flex items-center gap-3">
          <!-- Simple SVG logo mark -->
          <svg class="logo-mark" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="2" y="6" width="20" height="12" rx="3" fill="#06b6d4" />
            <path d="M6 12h12" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" />
          </svg>
          <div>
            <div class="text-lg font-bold">The Promise</div>
            <div class="text-xs text-slate-500 -mt-1">Full e‑commerce, services & products</div>
          </div>
        </a>
        <nav class="hidden md:flex gap-6 items-center">
          <a href="#products" class="hover:text-teal-600">Products</a>
          <a href="#services" class="hover:text-teal-600">Services</a>
          <a href="#contact" class="text-white bg-teal-600 px-4 py-2 rounded-lg hover:opacity-95">Contact</a>
        </nav>
        <div class="md:hidden">
          <!-- simple mobile placeholder -->
          <button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')">Menu</button>
        </div>
      </div>
      <div id="mobile-menu" class="hidden px-6 pb-4 md:hidden">
        <a href="#products" class="block py-2">Products</a>
        <a href="#services" class="block py-2">Services</a>
        <a href="#contact" class="block py-2">Contact</a>
      </div>
    </header>

    <main class="mx-auto max-w-6xl px-6 pt-8">
      <!-- Hero -->
      <section class="grid md:grid-cols-2 gap-8 items-center py-12">
        <div>
          <h1 class="text-4xl md:text-5xl font-extrabold leading-tight">The Promise — Your trusted partner for products & services</h1>
          <p class="mt-4 text-slate-600">We provide a wide range of products, domestic manpower, CSC services and retail solutions. Quality, reliability and customer-first approach — that's our promise.</p>

          <div class="mt-6 flex gap-3">
            <a href="#products" class="bg-teal-600 text-white px-5 py-3 rounded-lg shadow hover:opacity-95">Shop Products</a>
            <a href="#services" class="border border-slate-200 px-5 py-3 rounded-lg">Explore Services</a>
          </div>

          <div class="mt-8 grid grid-cols-2 gap-3 text-sm">
            <div class="p-3 bg-white rounded-lg shadow-sm">
              <div class="font-semibold">Secure Payments</div>
              <div class="text-slate-500 text-xs">Multiple payment options & safe checkout</div>
            </div>
            <div class="p-3 bg-white rounded-lg shadow-sm">
              <div class="font-semibold">Verified Staff</div>
              <div class="text-slate-500 text-xs">Background-checked domestic helpers & service providers</div>
            </div>
          </div>
        </div>
        <div>
          <!-- Illustration / product mockup -->
          <div class="w-full h-64 md:h-80 rounded-2xl bg-gradient-to-br from-teal-400 to-cyan-500 flex items-center justify-center text-white">
            <div class="text-center px-6">
              <div class="text-2xl font-bold">Start selling or hiring today</div>
              <div class="mt-2 text-sm opacity-90">A simple platform to list products and services — built for small businesses and homemakers.</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Products -->
      <section id="products" class="py-6">
        <h2 class="text-2xl font-bold">Featured Products</h2>
        <p class="text-sm text-slate-600 mt-1">Handpicked items — ready to ship.</p>

        <div class="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {% for p in products %}
          <div class="bg-white rounded-lg shadow hover:shadow-md overflow-hidden">
            <div class="h-40 bg-slate-100 flex items-center justify-center"> <!-- image placeholder -->
              <div class="text-slate-400">Image</div>
            </div>
            <div class="p-4">
              <div class="font-semibold">{{ p.name }}</div>
              <div class="text-sm text-slate-500 mt-1">{{ p.desc }}</div>
              <div class="mt-3 flex items-center justify-between">
                <div class="font-bold">{{ p.price }}</div>
                <a href="#contact" class="text-sm bg-teal-600 text-white px-3 py-1 rounded">Buy</a>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </section>

      <!-- Services -->
      <section id="services" class="py-10">
        <h2 class="text-2xl font-bold">Services We Offer</h2>
        <p class="text-sm text-slate-600 mt-1">From staffing to retail promotions — we've got you covered.</p>

        <div class="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6">
          {% for s in services %}
          <div class="p-6 bg-white rounded-lg shadow-sm">
            <div class="font-semibold text-lg">{{ s.title }}</div>
            <div class="text-sm text-slate-500 mt-2">{{ s.long }}</div>
            <div class="mt-4">
              <a href="#contact" class="text-sm bg-teal-600 text-white px-3 py-2 rounded">Get Started</a>
            </div>
          </div>
          {% endfor %}
        </div>
      </section>

      <!-- Contact / CTA -->
      <section id="contact" class="py-12">
        <div class="bg-gradient-to-r from-white to-slate-50 p-6 rounded-lg shadow-sm">
          <div class="md:flex md:items-center md:justify-between">
            <div>
              <h3 class="text-xl font-bold">Want to list a product or hire staff?</h3>
              <p class="text-sm text-slate-600 mt-1">Contact our team and we'll help you get started — marketplace listings, staffing support, and more.</p>
            </div>
            <div class="mt-4 md:mt-0">
              <a href="mailto:contact@thepromise.example" class="bg-white border border-teal-600 text-teal-600 px-5 py-3 rounded-lg font-medium">Email Us</a>
            </div>
          </div>
        </div>
      </section>

      <footer class="py-8 text-center text-sm text-slate-500">
        © {{ year }} The Promise — All rights reserved. | Built with ❤️ for small businesses
      </footer>
    </main>

    <!-- small script to support some interactivity or future expansion -->
    <script>
      // placeholder for future JS
      console.log('The Promise landing loaded');
    </script>
  </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, products=PRODUCTS, services=SERVICES, year=2025)

if __name__ == '__main__':
    app.run(debug=True)
