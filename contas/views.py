from django.shortcuts import render, redirect
from .forms import UsuarioCPFForm, LoginCPFForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def cadastrar_usuario_comum(request):
    if request.method == 'POST':
        form = UsuarioCPFForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_cpf')
    else:
        form = UsuarioCPFForm()
    return render(request, 'contas/cadastro.html', {'form': form})

def login_cpf(request):
    if request.method == 'POST':
        form = LoginCPFForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('painel')
    else:
        form = LoginCPFForm()
    return render(request, 'contas/login.html', {'form': form})

@login_required
def painel(request):
    return render(request, 'contas/painel.html')
