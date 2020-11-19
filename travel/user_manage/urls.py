
from django.urls import path
# from django.contrib import admin
# from django.views.generic import TemplateView,ListView
from .views import *
# from myapp.models import package

urlpatterns = [
    path('register/client/',client_registration,name="client_register_page"),
    path('register/admin/',admin_registration,name="admin_register_page"),
    path('client-register/',register_client,name="client_register"),
    path('admin-register/',register_admin,name="admin_register"),
]