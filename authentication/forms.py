from django import forms
from matplotlib import widgets
from .models import *

class User_Forms(forms.ModelForm):
    class Meta:
        model = Authentication
        fields = [
            'Username',
            'Password',
            ]
        widgets={
            'Username': forms.TextInput(attrs={'class':'form-control'}),
            'Password': forms.TextInput(attrs={'class':'form-control'})
        }
