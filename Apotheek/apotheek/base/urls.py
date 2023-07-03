from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("hello/", views.say_hello, name="hello"),
    path("nameform/", views.nameform, name="nameform"),
]