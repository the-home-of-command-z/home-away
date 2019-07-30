from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from core.models import Device
from django.views.decorators.http import require_http_methods
from .forms import RegisterDeviceForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

# Create your views here.

@csrf_exempt
@require_http_methods(['GET'])
def endpoint(request, username):
    userdata = Device.objects.filter(user=request.user)
    datalist = list(userdata.values('url', 'access_token'))
    return HttpResponse(json.dumps(datalist))


@login_required
def register_device(request):
    user = request.user
    if request.method == 'POST':
        form = RegisterDeviceForm(request.POST)
        if form.is_valid():
            f = form.save()
            return HttpResponseRedirect(reverse('registration-success'))
    else:
        form = RegisterDeviceForm()

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'register_device.html', context)

@login_required
def registration_success(request):
    return render(request, 'registration_success.html')


