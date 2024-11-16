from django.shortcuts import render
 # Views baseadas em funções (renderização)

def home(request):
    return render(request, 'index.html')

def cadastro_view(request):
    return render(request, 'index_cad.html')

def sucess_page(request):
    return render(request, 'index_sucess.html')

def participante_page(request):
    return render(request, 'index_participante.html')

