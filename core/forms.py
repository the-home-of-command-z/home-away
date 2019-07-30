from django.forms import ModelForm
from core.models import Device

class RegisterDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['url', 'access_token']