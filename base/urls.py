from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('works/', views.works),
    path('feedback/', views.feedback),
    path('create/', views.get_feedback),
]