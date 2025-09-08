from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # homepage global
    path('accounts/', include('allauth.urls')), # ADICIONE ESTA LINHA
    path('usuarios/', include('usuarios.urls')),
    path('anatomia/', include('anatomia.urls')),
    path('sistema_osseo/', include('sistema_osseo.urls')),
    path('sistema_muscular/', include('sistema_muscular.urls')),
    path('sistema_nervoso/', include('sistema_nervoso.urls')),
    path('sistema_cardiovascular/', include('sistema_cardiovascular.urls')),
    path('sistema_respiratorio/', include('sistema_respiratorio.urls')),
    path('sistema_digestivo/', include('sistema_digestivo.urls')),
    path('sistema_urinario/', include('sistema_urinario.urls')),
    path('sistema_endocrino/', include('sistema_endocrino.urls')),
    path('sistema_tegumentar/', include('sistema_tegumentar.urls')),
    path('sistema_reprodutor/', include('sistema_reprodutor.urls')),
    path('sistema_hematopoietico/', include('sistema_hematopoietico.urls')),
    path('metabolismo/', include('metabolismo.urls')),
    path('psicologia/', include('psicologia.urls')),
    path('simbologia/', include('simbologia.urls')),
]
