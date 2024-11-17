from django.urls import path, include
from app.views.templates import home_view, cadastro_view, participante_view, sucess_view, perfil_view, edit_view, carteirinha_view, atividade_detalhes
from app.views.qrcode import gerar_qrcode 
from app.views.api import ParticipanteListView, ParticipanteDetailView

urlpatterns = [
    path('', home_view, name='home'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('participante/', participante_view, name='participante'),
    path('sucesso/', sucess_view, name='sucesso'),
    path('perfil/', perfil_view, name='perfil'),
    path('edit_perfil/', edit_view, name='edit_perfil'),
    path('carteirinha/', carteirinha_view, name='carteirinha'),
    path('qrcode/<str:cpf>/', gerar_qrcode, name='gerar_qrcode'),
    path('atividade/<int:atividade_id>/',atividade_detalhes, name='atividade_detalhes'),

    #path da api
    path('participantes/', ParticipanteListView.as_view(), name='participante-list'),  # Endpoint para listar e cadastrar participantes
    path('participantes/<int:pk>/', ParticipanteDetailView.as_view(), name='participante-detail'),  # atualizar e deletar um participante
]
