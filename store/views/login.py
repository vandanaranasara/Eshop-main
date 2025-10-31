from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    def get(self, request):
        # Store return URL (if user came from /cart or any protected page)
        return_url = request.GET.get('return_url')
        request.session['return_url'] = return_url
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            
            if flag:
                # Save customer info in session
                request.session['customer'] = customer.id
                request.session['user_type'] = customer.user_type 
                
                if request.session['user_type'] == 'buyer' :
                    return redirect('homepage')
                else :
                    return redirect('seller_dashboard')

            else:
                error_message = 'Invalid password!'
        else:
            error_message = 'Email not found!'

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
