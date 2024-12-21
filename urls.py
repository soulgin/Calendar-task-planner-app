from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_month, name='view_month'),
    path('add_task/', views.add_task, name='add_task'),
]
