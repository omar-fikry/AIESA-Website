from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('<slug:slug>/', views.training_detail, name='training_detail'),
]