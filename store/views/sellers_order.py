from django.shortcuts import render, redirect
from store.models.orders import Order
from store.models.customer import Customer
from django.views import View
from store.tasks import send_order_delievered_email_task

class ManageOrders(View):
    def get(self, request):
        user_type = request.session.get('user_type')

        # Only sellers can access
        if user_type != 'seller':
            return redirect('homepage')

        # Show all orders (you can filter by seller products if you add a seller field in Products)
        orders = Order.objects.all().order_by('-date')
        return render(request, 'manage_orders.html', {'orders': orders})

    def post(self, request):
        user_type = request.session.get('user_type')

        # Security check again
        if user_type != 'seller':
            return redirect('homepage')

        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return redirect('manage_orders')
        
        previous_status = order.status

        # Update status
        order.status = new_status
        order.save()
    
        return redirect('manage_orders')

