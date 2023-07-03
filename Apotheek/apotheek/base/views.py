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
