from django.contrib import admin
from django.urls import path,include
from . import views
# from rest_framework.routers import BaseRouter

# router = BaseRouter()

# router.register(r'advocates',views.AdvocateDetail.as_view)


urlpatterns = [
    path('',views.endpoints),
    path('advocates/',views.advocate_list),
    # path('advocates/<str:username>/',views.advocate_detail),
    path('advocates/<str:username>/',views.AdvocateDetail.as_view()),
    path('add_advocate',views.add_advocate)
]
