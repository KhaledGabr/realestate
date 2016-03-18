from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.homepage ),   # no homepage for the dashbaord at the moment
    
    
    
    
    url(r'^create/$', views.create ),
    url(r'^list/$', views.list),
    url(r'^detail/(?P<id>\d+)$', views.detail ),
    url(r'^update/$', views.update ),
    url(r'^delete/$', views.delete ),
    

]
