from django.shortcuts import render

def dashboard(request):
    return render(request, 'sistema_cardiovascular/dashboard.html')
