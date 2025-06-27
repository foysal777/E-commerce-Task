
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/' , include('myapp.urls')),
    path('product/' , include('product.urls')),
    path('striped/' , include('striped.urls')),
    
]
