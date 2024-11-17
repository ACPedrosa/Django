from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import Atividade
 # Views baseadas em funções (renderização)

def home_view(request):
    return render(request, 'index.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')

def login_view(request):
    return render(request, 'login.html') 

def sucess_view(request):
    return render(request, 'sucesso_cad.html')

@login_required
def participante_view(request):
    atividades = Atividade.objects.all()  # Recupera todas as atividades
    return render(request, 'participante.html', {'atividades': atividades})

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')

@login_required
def edit_view(request):
    return render(request, 'edit_perfil.html')

@login_required
def carteirinha_view(request):
    return render(request, 'carteirinha.html')

@login_required
def historico_view(request):
    return render(request, 'historico.html')

@login_required
def atividade_detalhes(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    turmas = atividade.turma_set.all()  # Recupera todas as turmas associadas à atividade
    return render(request, 'atividade.html', {'atividade': atividade, 'turmas': turmas})
