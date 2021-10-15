#import phone_field
from django import forms
from .models import *


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'make an UN'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'write Ur F-name'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'write Ur L-name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'write an email'}))
    password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'placeholder': 'make a PW'}))
    password_check = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'placeholder': 'write the PW '
                                                                                                     'U made'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('username exists.')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exists.')
        return email

    def clean_password_check(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password_check']
        if pass1 != pass2:
            raise forms.ValidationError('enter a same password twice.')
        elif len(pass2) < 8:
            raise forms.ValidationError('password is too short.')
        return pass2


class UserLoginForm(forms.Form):
    user_name_or_email = forms.CharField(max_length=20,
                                         widget=forms.TextInput(attrs={'placeholder': 'write Ur UN or email'}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'placeholder': 'write Ur PW'}))

    def clean_user_name_or_email(self):
        user_name_or_email = self.cleaned_data['user_name_or_email']
        if User.objects.filter(email=user_name_or_email).exists():
            pass
        elif User.objects.filter(username=user_name_or_email).exists():
            pass
        else:
            raise forms.ValidationError('user name or email does not exist.')
        return user_name_or_email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_num', 'address']

# class locationgetform(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = ['user','phone_num','x','y']
