from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from core.models import Device
from django.views.decorators.http import require_http_methods
from .forms import RegisterDeviceForm, editRegistration
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from django.urls import reverse
from django.shortcuts import get_object_or_404


# Create your views here.

@csrf_exempt
@require_http_methods(['GET'])
def endpoint(request):
    user_id = request.headers['auth']
    userdata = Device.objects.filter(user__username=user_id)
    datalist = list(userdata.values('url', 'access_token'))
    return HttpResponse(json.dumps(datalist))


@login_required(login_url='/')
def register_device(request):
    user = request.user
    if request.method == 'POST':
        form = RegisterDeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save()
            return HttpResponseRedirect(reverse('registration-success'))
    else:
        form = RegisterDeviceForm()

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'register_device.html', context)

@login_required(login_url='/')
def edit_registration(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        form = editRegistration(request.POST)
        if form.is_valid():
            device.url = form.cleaned_data['url']
            device.access_token = form.cleaned_data['access_token']
            device.save()
            return HttpResponseRedirect(
                reverse('registration-success'))

    else:
        form = editRegistration(
            initial={
                'url': device.url,
                'access_token': device.access_token,

            })

    context = {
        'form': form,
        'device': device,
    }

    return render(request, 'edit_registration.html', context)

@login_required(login_url='/')
def registration_success(request):
    return render(request, 'registration_success.html')

# def homepage(request):
#     device = get_object_or_404(Device)
#     return render(request, 'homepage.html', {'device': device})
def homepage(request):
    return render(request, 'homepage.html')

def help_page(request):
    return render(request, 'help.html')
