from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('Normal Attar',views.Normal_Attar,name='Normal Attar'),
    path('Special Attar',views.Special_Attar,name='Special Attar'),
    path('Premium Attar',views.Premium_Attar,name='Premium Attar'),
    path('Normal Perfumes',views.Normal_Perfumes,name='Normal Perfumes'),
    path('Special Perfumes',views.Special_Perfumes,name='Special Perfumes'),
    path('Customizations',views.Customizations,name='Customizations'),


]
