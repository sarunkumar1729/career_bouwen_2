from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



# class JobSeekerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Userprofile
#         fields = ['full_name','job_title', 'email', 'contact_number', 'location','qualification','profile_pic', 'cv']
#         widgets = {
#             'profile_pic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
#             'cv': forms.ClearableFileInput(attrs={'accept': 'application/pdf, application/msword'}),
#         }

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['full_name','job_title', 'email', 'contact_number', 'location','qualification','profile_pic', 'cv']
        labels = {
            'job_title': 'Profession',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.Select(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf, application/msword'}),
        }

    
    
# class EmployerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Userprofile
#         fields = ['company_name', 'company_category', 'email','company_address','contact_number','profile_pic']
#         widgets = {
#             'profile_pic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
#         }

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['company_name', 'company_category', 'email','company_address','contact_number','profile_pic']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_category': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
        }

        
# class AddJobForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ['title',   'company_name', 'company_address', 'company_zipcode', 'company_place', 'company_country', 'company_size','description']

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'company_address', 'company_zipcode', 'company_place', 'company_country', 'company_size', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control'}),
            'company_zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'company_place': forms.TextInput(attrs={'class': 'form-control'}),
            'company_country': forms.TextInput(attrs={'class': 'form-control'}),
            'company_size': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


# class ApplicationForm(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = ['content', 'experience']
#         widgets = {
#             'content': forms.Textarea(attrs={'rows': '4'}),  # Adjust the rows value as needed
#             'experience': forms.Textarea(attrs={'rows': '4'}),  # Adjust the rows value as needed
#         }
#         labels = {
#             'content':'Message'
#         }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),  # Adjust the rows value as needed
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),  # Adjust the rows value as needed
        }
        labels = {
            'content': 'Message',
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
