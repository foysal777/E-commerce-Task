from django.shortcuts import render
from django.conf import settings 
from rest_framework.decorators import api_view,permission_classes
# Create your views here.
import stripe
from rest_framework.permissions import AllowAny
from .models import MyProfile
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    mypp = MyProfile.objects.create(user=request.user)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items = [{
            'price':'price_1RdiTU4Ft3OiftBENmAiWovw',
            'quantity' : 1,
        }],
        mode='subscription',
        success_url ='http://localhost:8000/striped/api/success/?session_id={CHECKOUT_SESSION_ID}', 
        cancel_url = 'http://localhost:8000/striped/api/cancel' , 
             
      )
 
    mypp.stripe_session_id = session.id
    mypp.save()
    return redirect(session.url)


# def success_url(request):
#     return render(request, 'success.html')

@api_view(['GET'])
@permission_classes([AllowAny])
def success_url(request):
    session_id = request.GET.get('session_id')
    print('hellloooooooooooooo')
    print(session_id)
    
    # if not session_id:
    #     return render(request,  {'msg' : 'not found session id'})
    try:
        myprofile = MyProfile.objects.get(stripe_session_id=session_id)
    
    except MyProfile.DoesNotExist:
        return render(request, 'cancel.html', {'m' :'not found'})
    
    myprofile.is_paid = True
    myprofile.save()
    return render(request, 'success.html')

def cancel_url(requset):
    return render(requset, 'cancel.html')