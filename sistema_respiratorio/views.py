from django.shortcuts import render

def dashboard(request):
    return render(request, 'sistema_respiratorio/dashboard.html')
