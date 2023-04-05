from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('loginUser', views.loginUser, name='login'),
    path('logoutUser', views.logoutUser, name='logout'),
    path('service', views.service, name='service'),
    path('contactus', views.contactus, name='contactus'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>',
         views.updaterecord, name='updaterecord'),
]

urlpatterns += staticfiles_urlpatterns()
