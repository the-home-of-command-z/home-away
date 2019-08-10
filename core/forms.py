from django.forms import ModelForm
from core.models import Device
from django import forms


class RegisterDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['url', 'access_token']

class editRegistration(forms.Form):
    url = forms.CharField(max_length=200)
    access_token = forms.CharField(max_length=1000)