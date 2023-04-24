
from django.contrib import admin

from django.urls import include, path
    
from movimientos.views import RegisterCreateView , RegisterListView , Sumar
from gastoS.views import index


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('',index , name='index'),
    path('sumar/',Sumar , name='sumar'),
    path('create_register/', RegisterCreateView.as_view(),name='create_register'),
    path('list_register/', RegisterListView.as_view(),name='list_register'),
   
   
  
]