from django.shortcuts import render
from django.conf import settings 
# Create your views here.
import stripe

from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items = [{
            'price':'price_1RdiTU4Ft3OiftBENmAiWovw',
            'quantity' : 1,
        }],
        mode='subscription',
        success_url ='http://localhost:8000/striped/api/success', 
        cancel_url = 'http://localhost:8000/striped/api/cancel' , 
             
      )
    return redirect(session.url)


def success_url(request):
    return render(request, 'success.html')

def cancel_url(requset):
    return render(requset, 'cancel.html')