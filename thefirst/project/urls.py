from project.views import *
from django.urls import path
import project

urlpatterns = [
    path('',home_page),
    path('about',about_page),
]