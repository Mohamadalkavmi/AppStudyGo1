"""
Definition of urls for StudyGoOffice.
""" 

from datetime import datetime
 
from django.urls import path 

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms ,views
from django.conf import settings
from django.conf.urls.static import  static
from django.conf import settings
 

urlpatterns = [
    path('register/', views.register, name='register'),      
    path('', views.home, name='home'),
    
    #path('logout_user/',  views.logout_user, name='logout_user'),    
    path('loginMain/', views.loginMain, name='loginMain'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('SendApplication/',views.SendApplication, name='SendApplication'), 
    
    path('newApplication/<username>/', views.newApplication, name='newApplication'),    
    path('officepage/<username>/', views.officepage, name='officepage'),
    path('officepageEmp/<username>/', views.officepageEmp, name='officepageEmp'),
    path('officepageView/<username>/', views.officepageView, name='officepageView'),
    path('officepageManager/<username>/', views.officepageManager, name='officepageManager'),
    path('officepageAdmin/<username>/', views.officepageAdmin, name='officepageAdmin'),
    
    path('studendata/<studentId>/', views.studendata, name='studendata'),
    path('studendataEmp/<studentId>/', views.studendataEmp, name='studendataEmp'),
    path('UpdateInfo/<username>/', views.UpdateInfo, name='UpdateInfo'),
    path('UpdateAdmin/<ids>/', views.UpdateAdmin, name='UpdateAdmin'),      
    

    path('seatslist/<username>/', views.seatslist, name='seatslist'),
    path('seatslistEmp/<username>/', views.seatslistEmp, name='seatslistEmp'),
    path('seatslistView/<username>/', views.seatslistView, name='seatslistView'),
    path('uploadfile/<username>/', views.uploadfile, name='uploadfile'),
    
    path('officepageEmp/', views.officepageEmp, name='officepageEmp'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),        
    path('logout_user/', LogoutView.as_view(next_page='/'), name='logout_user'),
    path('admin/', admin.site.urls),        
    path('import_csv/',views.import_csv , name ='import_csv'),  
   
    ]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
    