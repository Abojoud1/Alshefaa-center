from django import forms
from matplotlib import widgets
from .models import *

class Patients_Forms(forms.ModelForm):
    class Meta:
        model = Patients
        fields = [
            'FName',
            'LName',
            'Gender',
            'BirthYear',
            'Weight',
            'CreditNumber',
            'Address',
            'Phon',
            'SocialStatus',
            'MedicalHistory',
        ]
        widgets={
            'FName': forms.TextInput(attrs={'class':'form-control'}),
            'LName': forms.TextInput(attrs={'class':'form-control'}),
            'Gender': forms.TextInput(attrs={'class':'form-control'}),
            'BirthYear': forms.DateInput(attrs={'class':'form-control'}),
            'Weight': forms.NumberInput(attrs={'class':'form-control'}),
            'CreditNumber': forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'Phon': forms.TextInput(attrs={'class':'form-control'}),
            'SocialStatus': forms.TextInput(attrs={'class':'form-control'}),
            'MedicalHistory': forms.TextInput(attrs={'class':'form-control'})
        }

