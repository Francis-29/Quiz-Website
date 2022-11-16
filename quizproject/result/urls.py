from django.urls import path
from . import views


urlpatterns = [
    path('result/<str:pk>/', views.result, name='result-view')
]