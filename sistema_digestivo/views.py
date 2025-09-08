from django.shortcuts import render

def dashboard(request):
    return render(request, 'sistema_digestivo/dashboard.html')
