
from django.urls import path

from . import views

urlpatterns = [
    path('test/<int:pk>/', views.IndexView.as_view()),
]