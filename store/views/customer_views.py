# store/views/customer_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.hashers import check_password
from store.models import Customer


class CustomLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Compare hashed password properly
        if not check_password(password, customer.password):
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Generate JWT tokens
        refresh = RefreshToken.for_user(customer)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "customer": {
                "id": customer.id,
                "email": customer.email,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "user_type": customer.user_type,
            }
        }, status=status.HTTP_200_OK)
