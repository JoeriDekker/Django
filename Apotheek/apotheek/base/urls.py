from django.urls import path, include
from . import views
from .views import CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', CustomPasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_changed', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('medicines/', views.medicines, name='medicines'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('update_medicine/<int:medicine_id>/', views.update_medicine, name='update_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('collections', views.collections, name='collections'),
    path('add_collection', views.add_collection, name='add_collection'),
    path('delete_collection/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('personal_collections/', views.personal_collections, name='personal_collections'),
    path('collect/<int:collection_id>', views.collect, name='collect'),
    path('collected-items/', views.collected_items, name='collected_items'),
    path('approve_collected_item/<int:item_id>/', views.approve_collected_item, name='approve_collected_item'),
    path('users_overview/', views.users_overview, name='users_overview'),
    path('user_collections/<int:user_id>/', views.user_collections, name='user_collections'),
]