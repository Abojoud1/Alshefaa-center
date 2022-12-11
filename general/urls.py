from django.urls import path
from . import views

urlpatterns = [
    path('categoryss', views.categorys, name='categoryss'),
    path('items', views.items, name='items'),
    path('additems', views.additem, name='additems'),
    path('removeitem/<int:id>', views.removeitem, name='removeitem'),
    path('updateitem/<int:id>', views.updateitem, name='updateitem'),
    path('addcategorys', views.addcategory, name='addcategorys'),
    path('removecategory/<int:id>', views.removecategory, name='removecategory'),
    path('updatecategory/<int:id>', views.updatecategory, name='updatecategory'),
]