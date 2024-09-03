from django.urls import path
from app_register_user import views

urlpatterns = [
    path('',views.home,name='home')
]
