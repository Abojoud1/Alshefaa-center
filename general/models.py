from django.db import models
from doctors.models import Superviser_doctor

# Create your models here.

class Categorys(models.Model):
    CatName=models.CharField(max_length=20,default='zzz')
    Superviser_id = models.ForeignKey(Superviser_doctor,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.CatName


class Items(models.Model):
    ItemName=models.CharField(max_length=20,default='zzz')

    def __str__(self):
        return self.ItemName
