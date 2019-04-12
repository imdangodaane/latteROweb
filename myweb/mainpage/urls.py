from django.urls import path, include
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
]
