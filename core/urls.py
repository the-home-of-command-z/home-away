from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('register_device/', views.register_device, name='register-device'),
    path('registration_success/', views.registration_success, name='registration-success'),
    
]