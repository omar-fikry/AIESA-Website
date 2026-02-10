from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('<slug:slug>/', views.activity_detail, name='activity_detail'),
]