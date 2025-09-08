from django.shortcuts import render

def dashboard(request):
    return render(request, 'sistema_muscular/dashboard.html')
