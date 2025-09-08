from django.shortcuts import render

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Você já pode fazer o login.')
            return redirect('usuarios:login') # Redireciona para nossa futura página de login
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})