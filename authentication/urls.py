from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('base/',views.base,name='base'),
    path('logouts', views.logout_user, name='logouts'),
    path('userss', views.users, name='userss'),
    path('removeuser/<int:id>', views.removeuser, name='removeuser'),
    path('updateuser/<int:id>', views.updateuser, name='updateuser'),
    path('addusers', views.adduser, name='addusers'),
]