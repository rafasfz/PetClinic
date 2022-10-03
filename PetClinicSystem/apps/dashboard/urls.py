from django.urls import path

from .views import dashbaord

urlpatterns = [
    path('', dashbaord, name='dashboard'),
]
