from django.urls import path

from app_1 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('report', views.report, name="report"),
]