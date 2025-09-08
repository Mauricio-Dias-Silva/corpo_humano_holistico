from django.shortcuts import render

def dashboard(request):
    return render(request, 'sistema_endocrino/dashboard.html')
