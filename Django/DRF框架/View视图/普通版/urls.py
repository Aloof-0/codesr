# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/31 11:48
@Auth ： 高冷Aloof
@File ：urls.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books/<int:pk>', views.BookAPIView2.as_view()),
]