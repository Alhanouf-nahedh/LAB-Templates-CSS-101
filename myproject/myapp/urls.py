from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/cv/', views.cv, name='cv'),
    path('ai/', views.ai, name='ai'),
]
