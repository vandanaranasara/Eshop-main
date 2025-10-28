from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    def get(self, request):
        # Store the return URL (if user came from /cart or any protected page)
        return_url = request.GET.get('return_url')
        request.session['return_url'] = return_url
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            # Check password validity
            flag = check_password(password, customer.password)
            if flag:
                # Save customer session
                request.session['customer'] = customer.id

                # Redirect to return_url if available
                return_url = request.session.get('return_url')
                if return_url:
                    request.session['return_url'] = None  # clear it
                    return HttpResponseRedirect(return_url)
                else:
                    return redirect('homepage')
            else:
                error_message = 'Invalid password!'
        else:
            error_message = 'Email not found!'

        # On login error, show message
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')

