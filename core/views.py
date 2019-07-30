from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from core.models import Device
from django.views.decorators.http import require_http_methods

# Create your views here.

@csrf_exempt
@require_http_methods(['GET'])
def endpoint(request):
    userdata = Device.objects.filter(user=Device.user)
    dictdata = model_to_dict(userdata)
    return JsonResponse(dictdata)
