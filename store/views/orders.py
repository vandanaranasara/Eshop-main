from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from store.tasks import send_order_delievered_email_task

class OrderView(View):


    def get(self , request ):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)
        orders = Order.get_orders_by_customer(customer)
        #print(orders)
        
                
        for order in orders:
            if order.status:
                send_order_delievered_email_task.delay(customer.email, customer.first_name)
                order.save()

        return render(request , 'orders.html'  , {'orders' : orders})
    
        
