from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("hello/", views.say_hello, name="hello"),
    path("nameform/", views.nameform, name="nameform"),
    path("profile/", views.profile, name="profile"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('medicines/', views.medicines, name='medicines'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('update_medicine/<int:medicine_id>/', views.update_medicine, name='update_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
]