from django.shortcuts import render,redirect
from . models import Report
from . forms import Report_Forms
from patients.forms import Patients_Forms
from doctors.forms import Doctor_Forms,Superviser_doctor_Forms
from general.forms import Categorys_Forms,Items_Forms
# from django.http import HttpResponse

# Create your views here.

def reports(request):
    search=Report.objects.all()
    date=None
    if 'search_date' in request.GET:
        date=request.GET['search_date']
        if date:
            search=search.filter(date__icontains=date)
    return render(request,'reports/reports.html',{'rep':search})

def addreport(request):
    if request.method =='POST':
        dataform=Report_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'reports/addreport.html',{'rep':Report_Forms})

def removereport(request,id):
    report_id=Report.objects.get(id=id)
    if request.method=='POST':
        report_id.delete()
        return redirect('reportss')
    return render(request,'reports/removereport.html')

def updatereport(request,id):
    report_id=Report.objects.get(id=id)
    if request.method=='POST':
        report_save=Report_Forms(request.POST,request.FILES,instance=report_id)
        if report_save.is_valid():
            report_save.save()
            return redirect('reportss')
    else:
        report_save=Report_Forms(instance=report_id)
    context={'form':report_save}
    return render(request,'reports/updatereport.html',context)

def viewallreportsbyday(request):
    search=Report.objects.all()
    date=None
    if 'search_date' in request.GET:
        date=request.GET['search_date']
        if date:
            search=search.filter(date__icontains=date)
    return render(request,'reports/viewallreportsbyday.html',{'rep':search})

def viewallreportsbypatient(request):
    search=Report.objects.all()
    name=None
    if 'search_name' in request.GET:
        date=request.GET['search_name']
        if name:
            search=search.filter(name__icontains=name)
    return render(request,'reports/viewallreportsbypatient.html',{'rep':search})


def viewreport(request,id):
     report_id=Report.objects.get(id=id)
     report_save=Report_Forms(instance=report_id)
     pat_id=report_id.patien_id
     pat_save=Patients_Forms(instance=pat_id)

     doc_id=report_id.doc_id
     doc_save=Doctor_Forms(instance=doc_id)

     cat_id=report_id.cat_id
     cat_save=Categorys_Forms(instance=cat_id)

     sup_id=cat_id.Superviser_id
     sup_save=Superviser_doctor_Forms(instance=sup_id)

     itm_id=report_id.item_id
     itm_save=Items_Forms(instance=itm_id)

     re=report_id.state
     mm=report_id.ImagePathstring

     context={'form':report_save,'ff':re,'im':mm,'pp':pat_save,"dd":doc_save,"cc":cat_save,"ss":sup_save,"ii":itm_save}
     return render(request,'reports/viewreport.html',context)



    

