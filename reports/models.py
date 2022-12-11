from distutils.command.upload import upload
from django.db import models
from general.models import Categorys,Items
from patients.models import Patients
from doctors.models import Doctor

# Create your models here.

class Report(models.Model):
    date = models.DateField(null=True)
    MatName=models.CharField(max_length=20,default='zzz')
    injection_method = models.CharField(max_length=20,null=True)
    injection_quantity = models.CharField(max_length=20,null=True)
    KV = models.DecimalField(max_digits=6,decimal_places=3,null=True)
    MAS = models.DecimalField(max_digits=6,decimal_places=3,null=True)
    ImagePathstring = models.ImageField(upload_to='photo/%y/%m/%d',null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=3,null=True)
    cat_id = models.ForeignKey(Categorys,on_delete=models.PROTECT,null=True)
    item_id =  models.ForeignKey(Items,on_delete=models.PROTECT,null=True)
    patien_id = models.ForeignKey(Patients,on_delete=models.PROTECT,null=True)
    doc_id = models.ForeignKey(Doctor,on_delete=models.PROTECT,null=True)
    patient_preparation = models.TextField(null=True) 
    state= models.TextField(null=True)

    def __str__(self):
        return self.patien_id
    