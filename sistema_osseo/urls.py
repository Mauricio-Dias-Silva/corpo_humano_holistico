from django.urls import path
from . import views

app_name = 'sistema_osseo'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
