from django.urls import path
from . import views

app_name = 'metabolismo'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
