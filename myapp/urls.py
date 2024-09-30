from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indepage),
    path('aboutus',views.aboutpage)

]