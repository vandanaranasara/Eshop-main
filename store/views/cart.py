from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products


class Cart(View):
    def get(self, request):
        # Check if user is logged in
        customer = request.session.get('customer')
        if not customer:
            # Redirect to login page with return URL
            return redirect(f'/login?return_url={request.path}')


        # Get cart from session
        cart = request.session.get('cart')
        if not cart:
            # If cart is empty, show empty cart message
            return render(request, 'cart.html', {'empty': True})

        # If cart exists, get product details
        ids = list(cart.keys())
        products = Products.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})
    

