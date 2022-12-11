
from django import forms
from matplotlib import widgets
from .models import Report

class Report_Forms(forms.ModelForm):
    class Meta:
        model=Report
        fields = [
            'date',
            'MatName',
            'injection_method',
            'injection_quantity',
            'KV',
            'MAS',
            'ImagePathstring',
            'price',
            'cat_id',
            'item_id',
            'patien_id',
            'doc_id',
            'patient_preparation',
            'state',
        ]
        widgets={
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'MatName': forms.TextInput(attrs={'class':'form-control'}),
            'injection_method': forms.TextInput(attrs={'class':'form-control'}),
            'injection_quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'KV': forms.NumberInput(attrs={'class':'form-control'}),
            'MAS': forms.NumberInput(attrs={'class':'form-control'}),
            'ImagePathstring': forms.FileInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'cat_id': forms.Select(attrs={'class':'form-control'}),
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'patien_id': forms.Select(attrs={'class':'form-control'}),
            'doc_id': forms.Select(attrs={'class':'form-control'}),
            'patient_preparation': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Textarea(attrs={'class':'form-control'})
        }