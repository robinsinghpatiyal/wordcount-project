
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('count/',views.count, name='count'), #name is only for html purpose so the change in url does not affect much
    path('about/',views.about, name='about'),
]
