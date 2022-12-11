from django.urls import path
from . import views


urlpatterns = [
    path('reportss', views.reports, name='reportss'),
    path('addreports', views.addreport, name='addreports'),
    path('removereport/<int:id>', views.removereport, name='removereport'),
    path('updatereport/<int:id>', views.updatereport, name='updatereport'),
    path('viewallreportsbydays', views.viewallreportsbyday, name='viewallreportsbydays'),
    path('viewallreportsbypatients', views.viewallreportsbypatient, name='viewallreportsbypatients'),
    path('viewreport/<int:id>', views.viewreport, name='viewreport'),
    
]