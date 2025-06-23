from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.endpoints),
    path('advocates/',views.advocate_list),
    path('advocates/<str:username>/',views.advocate_detail),
    path('add_advocate',views.add_advocate)
]
