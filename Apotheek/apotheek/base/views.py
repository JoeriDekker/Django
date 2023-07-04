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



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
        
    context = {"form": form}

    return render(request, "registration/register.html", context)

def index(request):
    return render(request, "base/index.html")

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
            return redirect('medicines')
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


def collections(request):
    collections_list = Collection.objects.all()
    context = {
        'collections': collections_list
    }
    return render(request, 'base/collections.html', context)

def add_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collections')
    else:
        form = CollectionForm()

    context = {
        'form': form
    }

    return render(request, 'base/add_collection_item.html', context)

def delete_collection(request, collection_id):
    collection = Collection.objects.get(pk=collection_id)
    collection.delete()
    return redirect('collections')

def personal_collections(request):
    collections = Collection.objects.filter(user=request.user, collected=False)
    context = {
        'collections': collections
    }
    return render(request, 'base/personal_collections.html', context)

def collect(request, collection_id):
    collection = Collection.objects.get(pk=collection_id)    
    collection.collected = True
    collection.save()
    return redirect('personal_collections')

def collected_items(request):
    collected_items = Collection.objects.filter(collected=True)
    context = {
        'collected_items': collected_items
    }
    return render(request, 'base/collected_items.html', context)

def approve_collected_item(request, item_id):
    item = Collection.objects.get(pk=item_id)
    item.collected_approved = True
    item.collected_approved_by = request.user
    item.save()
    return redirect('collected_items')

def nameform(requests):
    form = NameForm()
    context = {"form": form}

    if requests.method == "POST":
        name = requests.POST.get("your_name")
        context["greeting"] = f"Welcome {name}!"

    return render(requests, "base/nameform.html", context)
