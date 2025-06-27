from django.urls import path
from .views import create_checkout_session, success_url, cancel_url

urlpatterns = [
     path('payment/' ,create_checkout_session,  name='stripe_checkout' ),
     path('api/success/' ,success_url,  name='success_url' ),
     path('api/cancel/' ,cancel_url,  name='cancel_url' )

]
