from django.urls import path
from . import views

urlpatterns = [
    path('result/<str:pk>/', views.result, name='result-view'),
    path('login/', views.user_login, name='login-view'),
    path('logout/', views.user_logout, name='logout-view'),
    path('register/', views.user_register, name='register-view'),
]
