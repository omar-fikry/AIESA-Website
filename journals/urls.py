from django.urls import path
from . import views

urlpatterns = [
    path('', views.journals, name='journals'),
    path('<slug:slug>/', views.journal_detail, name='journal_detail'),
]