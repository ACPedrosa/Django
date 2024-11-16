import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.models import Participante

def gerar_qrcode(request, cpf):
    # Recupera o participante com o CPF
    participante = get_object_or_404(Participante, usuario__cpf=cpf)

    # Gera o QR Code com o CPF do usuário
    qr = qrcode.make(participante.usuario.cpf)

    # Prepara a resposta para a imagem
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response
