from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order

from django.core.mail import send_mail
from django.conf import settings
from store.models.customer import Customer
from store.tasks import send_order_confirm_email_task


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=customer,
                          product=product,
                          price=product.price,
                          address=address,
                          pincode=pincode,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        
        send_order_confirm_email_task.delay(customer.email, 
                                            customer.first_name)
        

        return redirect('cart')
    
