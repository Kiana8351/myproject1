from project.views import *
from django.urls import path
import project
app_name = 'project'
urlpatterns = [
    path('',home_page,name='index'),
    path('about',about_page,name='about'),
    path('contact',contact_page,name='contact'),
    path('test',test_view,name='test')
]