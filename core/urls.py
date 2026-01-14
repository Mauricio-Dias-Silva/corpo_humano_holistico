from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('galaxy/', views.galaxy_page, name='galaxy'),
    path('pacientes/diagnostico/', views.diagnostico_view, name='diagnostico'),
    path('mapa3d/', views.body_map, name='mapa3d'),
    path('holograma/', views.hologram_view, name='holograma'),
    path('api/pubmed/', views.pubmed_search, name='pubmed_search'),
]