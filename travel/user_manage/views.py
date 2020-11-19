from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import *
from django.urls import reverse
# Create your views here.
def client_registration(request):
    return render(request,'client_register.html')


def admin_registration(request):
    return render(request,'admin_register.html')


def register_client(request):
    if request.method!='POST':
        return render(request,'index.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        client_types = request.POST.get('client_types')
        try:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,client_types=client_types)
            user.save()
            user.groups.set('2')
            messages.success(request,'successfully registered as client')
            return HttpResponseRedirect(reverse('client_register_page', ))
        except ValueError:
            messages.error(request,'faild to add')
            return HttpResponseRedirect(reverse('client_register_page', ))


def register_admin(request):
    if request.method!='POST':
        return render(request,'index.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        admin_types = request.POST.get('admin_types')
        try:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,admin_types=admin_types)
            user.save()
            user.groups.set('1')
            messages.success(request,'successfully registered as admin')
            return HttpResponseRedirect(reverse('admin_register_page', ))
        except:
            messages.error(request,'faild to add')
            return HttpResponseRedirect(reverse('admin_register_page', ))       
    






# def register_client(request):
#     if request.method!='POST':
#         return render(request,'index.html')
#     else:
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('psw')
#         client_types = request.POST.get('client_types')
#         user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,client_types=client_types)
#         user.groups.set('2')
#         user.save()
#         messages.success(request,'successfully registered')
#         return HttpResponseRedirect(reverse('user_manage:index', ))
#         # except:
#         #     messages.error(request,'faild to add')
#         #     return HttpResponseRedirect(reverse('user_manage:index', ))
            