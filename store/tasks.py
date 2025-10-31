from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email_task( user_email, customer_name):
    send_mail(
        subject='Welcome to Eshop!',
        message=f'''Hello {customer_name},
        Thank You for registering with Eshop. We are glad to have you!
        Please click on the below link to confirm your registration.
        http://localhost:8000/login/
        
        Warm regards,
        The Eshop Team
        http://localhost:8000/store/''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
    
