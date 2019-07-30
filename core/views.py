from django.shortcuts import render
from core.models import Device
from .forms import RegisterDeviceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
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


