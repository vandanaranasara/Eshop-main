from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email_task(user_email):
    send_mail(
        subject='Welcome to Eshop!',
        message='Thank you for registering with Eshop. We are glad to have you!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
    
@shared_task
def send_order_confirm_email_task(user_email, customer_name):
    send_mail(
        subject='Order Confirmation - Eshop',
        message=f'Hi {customer_name}, Your order has been placed successfully!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
