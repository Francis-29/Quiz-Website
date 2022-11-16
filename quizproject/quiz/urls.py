from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-view'),
    path('quiz/<str:pk>/', views.quiz_info, name='quiz-info-view'),
    path('quiz/test/<str:pk>/', views.quiz_test, name='quiz-test-view'),
]