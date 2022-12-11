from django import forms
from matplotlib import widgets
from .models import *

class Categorys_Forms(forms.ModelForm):
    class Meta:
        model = Categorys
        fields = [
            'CatName',
            'Superviser_id',
            ]
        widgets={
            'CatName': forms.TextInput(attrs={'class':'form-control'}),
            'Superviser_id': forms.Select(attrs={'class':'form-control'})
        }

class Items_Forms(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            'ItemName',
        ]
        widgets={
            'ItemName': forms.TextInput(attrs={'class':'form-control'})
        }