from tabnanny import verbose
from django.db import models

# Create your models here.

class Specializations(models.Model):
    SpeName=models.CharField(max_length=20,default='zzz')

    def __str__(self):
        return self.SpeName


class Doctor(models.Model):
    Name=models.CharField(max_length=20,default='zzz')
    Address=models.CharField(max_length=20,null=True)
    Phon=models.CharField(max_length=20,null=True)
    Spe_id = models.ForeignKey(Specializations,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.Name

class Superviser_doctor(models.Model):
    Name=models.CharField(max_length=20,default='zzz')
    Phon=models.CharField(max_length=20,null=True)
    WorkStart=models.CharField(max_length=20,null=True)
    WorkEnd=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.Name