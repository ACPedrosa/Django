from django.contrib.auth.decorators import login_required
from django.shortcuts import render
 # Views baseadas em funções (renderização)

def home_view(request):
    return render(request, 'index.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')

def login_view(request):
    return render(request, 'login.html') 

@login_required
def participante_view(request):
    return render(request, 'participante.html')

@login_required
def sucess_view(request):
    return render(request, 'sucesso_cad.html')

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')

@login_required
def carteirinha_view(request):
    return render(request, 'carteirinha.html')

