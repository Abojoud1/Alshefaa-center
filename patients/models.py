from django.db import models

# Create your models here.

class Patients(models.Model):
    FName=models.CharField(max_length=20,default='zzz')
    LName=models.CharField(max_length=20,default='zzz')
    Gender=models.CharField(max_length=20,null=True)
    BirthYear=models.DateField(null=True)
    Weight=models.IntegerField(null=True)
    CreditNumber=models.IntegerField(null=True)
    Address=models.CharField(max_length=20,null=True)
    Phon=models.CharField(max_length=20,null=True)
    SocialStatus=models.CharField(max_length=20,null=True)
    MedicalHistory=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.FName
