"""homeaway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('core/', include('core.urls')),
    # path('', RedirectView.as_view(url='/core/', permanent=True)),
    path('accounts/', include('allauth.urls')),
    path('api/', views.endpoint),
    path('register_device/', views.register_device, name='register-device'),
    path('registration_success/', views.registration_success, name='registration-success'),
    path('', views.homepage, name="homepage"),
    path('help/', views.help_page, name='helppage'),
    path('edit_registration/<int:pk>/', views.edit_registration, name='edit-registration'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 