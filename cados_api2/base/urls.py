from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework.routers import BaseRouter

# router = BaseRouter()

# router.register(r'advocates',views.AdvocateDetail.as_view)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), 
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.endpoints),
    path('advocates/',views.advocate_list),
    # path('add_advocate',views.add_advocate)
    # path('advocates/<str:username>/',views.advocate_detail),
    path('advocates/<str:username>/',views.AdvocateDetail.as_view()),
    
    #companies/
    #companies/:id
    path('companies/',views.companies_list)
]
