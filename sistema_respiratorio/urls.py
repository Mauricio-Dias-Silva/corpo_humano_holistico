from django.urls import path
from . import views

app_name = 'sistema_respiratorio'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
