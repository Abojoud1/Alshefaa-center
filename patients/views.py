from django.shortcuts import render,redirect
from . models import *
from .forms import *

# Create your views here.

def patients(request):
    search=Patients.objects.all()
    FName=None
    if 'search_fname' in request.GET:
        FName=request.GET['search_fname']
        if FName:
            search=search.filter(FName__icontains=FName)
    return render(request,'patients/patients.html',{'pat':search})

def addpatient(request):
    if request.method =='POST':
        dataform=Patients_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'patients/addpatient.html',{'pat':Patients_Forms})

def removepatient(request,id):
    patient_id=Patients.objects.get(id=id)
    if request.method=='POST':
        patient_id.delete()
        return redirect('patientss')
    return render(request,'patients/removepatient.html')

def updatepatient(request,id):
    patient_id=Patients.objects.get(id=id)
    if request.method=='POST':
        patient_save=Patients_Forms(request.POST,request.FILES,instance=patient_id)
        if patient_save.is_valid():
            patient_save.save()
            return redirect('patientss')
    else:
        patient_save=Patients_Forms(instance=patient_id)
    context={'form':patient_save}
    return render(request,'patients/updatepatient.html',context)
