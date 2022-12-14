from email.mime import image
from pyexpat import model
from random import choices
from select import select
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError
from .widget import DatePickerInput

from django.forms import ModelForm, Select

class RequisitionForm(ModelForm):
    req_hidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Requisition
        fields = '__all__'
        widgets = {
            'date_of_delivery' : DatePickerInput(),
            
            
        }

    send_to = forms.ModelMultipleChoiceField(
        queryset=NewUser.objects.all(),
        widget=forms.SelectMultiple,
        
    )
    # file = forms.FileField(
    #     widget=forms.ClearableFileInput(attrs={'multiple': True})
    #     )
    

class MultiFileForm(ModelForm):
    file_hidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = MultiFile
        # RequisitionForm.Meta.fields + 
        fields = ['file',]

    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
        )

class MultiNoteForm(ModelForm):
    note_hidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = MultiNote
        # RequisitionForm.Meta.fields + 
        fields = ['note']

    



class UpdateForm(ModelForm):
    update_hidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Requisition
        fields = ['date_of_delivery', 'status']
        widgets = {
            'date_of_delivery' : DatePickerInput(),
            
            
        }

    


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username','first_name', 'last_name', 'email','password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        

    allowed_domain = ['bdren.net.bd']

    def clean_email(self):
        email_doamin = self.cleaned_data['email'].split('@')[-1]
       

        if email_doamin not in self.allowed_domain:
            raise forms.ValidationError("Please supply an email address provided by BdREN.")
        
        return self.cleaned_data['email']



class UpdateProfileForm(ModelForm):
    class Meta:
        model = NewUser
        fields = [ 'phone', 'image']
        
