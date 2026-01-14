from django.contrib import admin
from django.urls import path, include
from core.views import homepage, galaxy_page, body_map, hologram_view, pubmed_search, organ_gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('galaxy/', galaxy_page, name='galaxy'),
    path('mapa3d/', body_map, name='body_map'),
    path('holograma/', hologram_view, name='holograma'),
    path('galeria/', organ_gallery, name='organ_gallery'),
    path('api/pubmed/', pubmed_search, name='pubmed_search'),
    path('pacientes/', include('pacientes.urls')),
    # path('accounts/', include('allauth.urls')),
]
