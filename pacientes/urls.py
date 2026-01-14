from django.urls import path
from .views import DiagnosticView

urlpatterns = [
    path('diagnostico/', DiagnosticView.as_view(), name='diagnostico'),
]
