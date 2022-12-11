from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('patientss', views.patients, name='patientss'),
    path('addpatients', views.addpatient, name='addpatients'),
    path('removepatient/<int:id>', views.removepatient, name='removepatient'),
    path('updatepatient/<int:id>', views.updatepatient, name='updatepatient'),
    
]