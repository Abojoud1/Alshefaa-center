from django.shortcuts import redirect, render
from . models import *
from .forms import *

# Create your views here.

def doctors(request):
    return render(request,'doctors/doctors.html',{'doc':Doctor.objects.all()})

def adddoctor(request):
    if request.method =='POST':
        dataform=Doctor_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'doctors/adddoctor.html',{'doc':Doctor_Forms})


def removedoctor(request,id):
    doctor_id=Doctor.objects.get(id=id)
    if request.method=='POST':
        doctor_id.delete()
        return redirect('doctorss')
    return render(request,'doctors/removedoctor.html')

def updatedoctor(request,id):
    doctor_id=Doctor.objects.get(id=id)
    if request.method=='POST':
        doctor_save=Doctor_Forms(request.POST,request.FILES,instance=doctor_id)
        if doctor_save.is_valid():
            doctor_save.save()
            return redirect('doctorss')
    else:
        doctor_save=Doctor_Forms(instance=doctor_id)
    context={'form':doctor_save}
    return render(request,'doctors/updatedoctor.html',context)


def supervisors(request):
    return render(request,'doctors/supervisors.html',{'sup':Superviser_doctor.objects.all()})

def addsupervisor(request):
    if request.method =='POST':
        dataform=Superviser_doctor_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'doctors/addsupervisor.html',{'sup':Superviser_doctor_Forms})

def addspecialization(request):
    if request.method =='POST':
        dataform=Specialization_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'doctors/addspecialization.html',{'spe':Specialization_Forms})

def specializations(request):
    return render(request,'doctors/specializations.html',{'spe':Specializations.objects.all()})


def removesupervisor(request,id):
    supervisor_id=Superviser_doctor.objects.get(id=id)
    if request.method=='POST':
        supervisor_id.delete()
        return redirect('supervisorss')
    return render(request,'doctors/removesupervisor.html')

def updatesupervisor(request,id):
    supervisor_id=Superviser_doctor.objects.get(id=id)
    if request.method=='POST':
        supervisor_save=Superviser_doctor_Forms(request.POST,request.FILES,instance=supervisor_id)
        if supervisor_save.is_valid():
            supervisor_save.save()
            return redirect('supervisorss')
    else:
        supervisor_save=Superviser_doctor_Forms(instance=supervisor_id)
    context={'form':supervisor_save}
    return render(request,'doctors/updatesupervisor.html',context)

