from django.urls import path
from . import views


urlpatterns = [
    path('', views.trustees, name='trustees'),
    path('<int:pk>/', views.trustee_detail, name='trustee_detail'),
]