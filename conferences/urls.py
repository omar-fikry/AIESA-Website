from django.urls import path
from . import views

urlpatterns = [
    path('', views.conferences, name='conferences'),
    path('<slug:slug>/', views.conference_detail, name='conference_detail'),
]