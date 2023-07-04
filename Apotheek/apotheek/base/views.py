import datetime

from django.shortcuts import *
from django.contrib import messages
from django.http import HttpResponse
from .models import Medicine, Collection
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



def say_hello(request):
    context = {"first_name": "Joeri", "last_name": "Dekker"}
    return render(request, "base/hello.html", context)

def index(request):
    return render(request, "base/index.html")

def nameform(requests):
    form = NameForm()
    context = {"form": form}

    if requests.method == "POST":
        name = requests.POST.get("your_name")
        context["greeting"] = f"Welcome {name}!"

    return render(requests, "base/nameform.html", context)


@login_required
def profile(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "base/profile.html", context)

@login_required
def update_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'base/update_profile.html', context)

@login_required
@staff_member_required
def medicines(request):
    medicines = Medicine.objects.all()
    context = {
        'medicines': medicines
    }
    return render(request, 'base/medicines.html', context)

@login_required
@staff_member_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicines')
    else:
        form = MedicineForm()

    context = {
        'form': form
    }

    return render(request, 'base/add_medicine.html', context)

@login_required
@staff_member_required
def update_medicine(request, medicine_id):
    medicine = Medicine.objects.get(pk=medicine_id)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)

    context = {
        'form': form,
        'medicine': medicine
    }

    return render(request, 'base/update_medicine.html', context)

@login_required
@staff_member_required
def delete_medicine(request, medicine_id):
    medicine = Medicine.objects.get(pk=medicine_id)
    medicine.delete()
    return redirect('medicines')