from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('doctorss', views.doctors, name='doctorss'),
    path('adddoctors', views.adddoctor, name='adddoctors'),
    path('removedoctor/<int:id>', views.removedoctor, name='removedoctor'),
    path('updatedoctor/<int:id>', views.updatedoctor, name='updatedoctor'),
    path('supervisorss', views.supervisors, name='supervisorss'),
    path('addsupervisors', views.addsupervisor, name='addsupervisors'),
    path('removesupervisor/<int:id>', views.removesupervisor, name='removesupervisor'),
    path('updatesupervisor/<int:id>', views.updatesupervisor, name='updatesupervisor'),
    path('addspecializations', views.addspecialization, name='addspecializations'),
    path('specializationss', views.specializations, name='specializationss'),
]