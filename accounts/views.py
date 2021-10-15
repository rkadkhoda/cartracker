from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .databasemanager import database_func,query_database_func
import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
"""
def user_get(request):
    if request.method == 'GET':
        print('get')

        id1 = User.objects.get(username=request.GET['user']).pk
        user1 = request.GET['user']
        phone = request.GET['phone']
        x = request.GET['x']
        y = request.GET['y']
        print(user1,User.objects.get(username=request.GET['user']))

        user10 = get_object_or_404(User, pk=User.objects.get(username=request.GET['user']).pk)
        print(user10)
        #Location.user=request.GET['user']

        user = authenticate(username='amin', password='amin10508')
        print(user)
        #print(request.user)
        Location(user=user,phone_num =phone,x=x,y=y).save()

        print(id1,user1,x,y)
        #form = locationgetform(request.GET, instance=request.user)
       # print(type(form))
        #if form.is_valid():
        #    print (form.cleaned_data['x'])
       #     print (form.cleaned_data['y'])
       # else:
       #     print('errrror', form.errors)

    return HttpResponse('yes')

"""




@csrf_exempt
#@method_decorator(csrf_exempt,name='')
def user_get(request):

    query_data={}
    if request.method == 'GET':
        try:
            #track, _ = Location.objects.get_or_create(domain=request.GET['domain'])
            #id = User.objects.get(username=request.GET['user']).pk
            #user = request.GET['user']
            phone_num = str(request.GET['phone'])
            x = str(request.GET['x'])
            y = str(request.GET['y'])
            database_func(phone_num,x,y)
            return HttpResponse('yes')

        except:
            phone_num = str(request.GET['phone'])
            x = str(request.GET['x'])
            y = str(request.GET['y'])

            database_func(phone_num,x,y)
            return HttpResponse('no')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            reg = User.objects.create_user(username=data['user_name'],
                                           email=data['email'],
                                           password=data['password_check'],
                                           first_name=data['first_name'],
                                           last_name=data['last_name']
                                           )
            reg.save()
            return redirect('accounts:user_login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user_name_or_email']),
                                    password=data['password'])
            except:
                user = authenticate(request, username=data['user_name_or_email'],
                                    password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('accounts:user_profile')

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


@login_required(login_url='accounts:user_login')
def user_logout(request):
    logout(request)
    return redirect('home:home')


@login_required(login_url='accounts:user_login')
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='accounts:user_login')
def user_update(request):
    if request.method == 'POST':
        pro_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        use_form = UserUpdateForm(request.POST, instance=request.user)
        if use_form and pro_form.is_valid():
            pro_form.save()
            use_form.save()
            return redirect('accounts:user_profile')
    else:
        pro_form = ProfileUpdateForm(instance=request.user.profile)
        use_form = UserUpdateForm(instance=request.user)
    context = {'pro_form': pro_form, 'use_form': use_form}
    return render(request, 'accounts/update.html', context)


@login_required(login_url='accounts:user_login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:user_profile')
        else:
            raise forms.ValidationError('password is wrong.')
    else:
        form = PasswordChangeForm(request.user)
        context = {'form': form}
    return render(request, 'accounts/password.html', context)


@login_required(login_url='accounts:user_login')
def user_location(request):
    # location = Location.objects.get(user_id=request.user.id)
    # context = {'location': location}
    # return render(request, 'accounts/location.html', context)
    profile = Profile.objects.get(user_id=request.user.id)
    phone_num = profile.phone_num
    kh=query_database_func(phone_num)
    context={'khoroji':kh}
    return render(request,'accounts/location.html',context)
