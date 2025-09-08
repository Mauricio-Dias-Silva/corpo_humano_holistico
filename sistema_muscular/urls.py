from django.urls import path
from . import views

app_name = 'sistema_muscular'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
