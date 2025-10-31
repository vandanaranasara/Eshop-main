from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    pincode = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} ({self.status})"

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
