from django.shortcuts import render

def dashboard(request):
    return render(request, 'sistema_osseo/dashboard.html')
