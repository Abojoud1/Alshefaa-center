from django import forms
from matplotlib import widgets
from .models import *

class Doctor_Forms(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'Name',
            'Address',
            'Phon',
            'Spe_id',
        ]
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'Phon': forms.TextInput(attrs={'class':'form-control'}),
            'Spe_id': forms.Select(attrs={'class':'form-control'})
        }

class Superviser_doctor_Forms(forms.ModelForm):
    class Meta:
        model = Superviser_doctor
        fields = [
            'Name',
            'Phon',
            'WorkStart',
            'WorkEnd',
        ]
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Phon': forms.TextInput(attrs={'class':'form-control'}),
            'WorkStart': forms.TextInput(attrs={'class':'form-control'}),
            'WorkEnd': forms.TextInput(attrs={'class':'form-control'})
        }

class Specialization_Forms(forms.ModelForm):
    class Meta:
        model = Specializations
        fields = [
            'SpeName',
        ]
        widgets={
            'SpeName': forms.TextInput(attrs={'class':'form-control'}),
        }
