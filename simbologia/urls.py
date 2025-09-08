from django.urls import path
from . import views

app_name = 'simbologia'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
