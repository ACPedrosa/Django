from django.urls import path, include
from app.views.templates import home_view, cadastro_view, participante_view, sucess_view, perfil_view, carteirinha_view
from app.views.qrcode import gerar_qrcode

urlpatterns = [
    path('', home_view, name='home'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('participante/', participante_view, name='participante'),
    path('sucesso/', sucess_view, name='sucesso'),
    path('perfil/', perfil_view, name='perfil'),
    path('carteirinha/', carteirinha_view, name='carteirinha'),
    path('qrcode/<str:cpf>/', gerar_qrcode, name='gerar_qrcode'),
]
