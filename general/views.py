from django.shortcuts import render,redirect
from . models import *
from .forms import *

# Create your views here.

def items(request):
    return render(request,'general/items.html',{'it':Items.objects.all()})

def additem(request):
    if request.method =='POST':
        dataform=Items_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'general/additem.html',{'it':Items_Forms})

def removeitem(request,id):
    item_id=Items.objects.get(id=id)
    if request.method=='POST':
        item_id.delete()
        return redirect('items')
    return render(request,'general/removeitem.html')

def updateitem(request,id):
    item_id=Items.objects.get(id=id)
    if request.method=='POST':
        item_save=Items_Forms(request.POST,request.FILES,instance=item_id)
        if item_save.is_valid():
            item_save.save()
            return redirect('items')
    else:
        item_save=Items_Forms(instance=item_id)
    context={'form':item_save}
    return render(request,'general/updateitem.html',context)

def categorys(request):
    return render(request,'general/categorys.html',{'cat':Categorys.objects.all()})

def addcategory(request):
    if request.method =='POST':
        dataform=Categorys_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'general/addcategory.html',{'cat':Categorys_Forms})

def removecategory(request,id):
    category_id=Categorys.objects.get(id=id)
    if request.method=='POST':
        category_id.delete()
        return redirect('categoryss')
    return render(request,'general/removecategory.html')


def updatecategory(request,id):
    category_id=Categorys.objects.get(id=id)
    if request.method=='POST':
        category_save=Categorys_Forms(request.POST,request.FILES,instance=category_id)
        if category_save.is_valid():
            category_save.save()
            return redirect('categoryss')
    else:
        category_save=Categorys_Forms(instance=category_id)
    context={'form':category_save}
    return render(request,'general/updatecategory.html',context)




