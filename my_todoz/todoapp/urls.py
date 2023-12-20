from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = 'index'),
    path('finish/<int:id>', views.finish, name='finishitem'),
    path('update/<int:id>', views.update, name='updateitem'),
]