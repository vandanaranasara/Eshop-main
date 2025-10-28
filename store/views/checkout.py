from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order

from django.core.mail import send_mail
from django.conf import settings
from store.models.customer import Customer


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        
        # Send confirmation email
        customer_obj = Customer.objects.get(id=customer)
        subject = 'Order Confirmation - Eshop'
        message = f'Hi {customer_obj.first_name}, your order has been placed successfully!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [customer_obj.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


        return redirect('cart')
    
