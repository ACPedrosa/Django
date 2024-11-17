from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Participante
from app.serializers import ParticipanteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated  # Melhor usar IsAuthenticated dependendo do seu caso


# Views da API (baseadas em classes)

class ParticipanteListView(APIView):
    permission_classes = [AllowAny]  # Altere para IsAuthenticated se necessário

    def get(self, request):
        participantes = Participante.objects.all()
        serializer = ParticipanteSerializer(participantes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ParticipanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipanteDetailView(APIView):
    permission_classes = [AllowAny]  # Altere para IsAuthenticated se necessário

    def get(self, request, pk):
        participante = get_object_or_404(Participante, pk=pk)
        serializer = ParticipanteSerializer(participante)
        return Response(serializer.data)

    def put(self, request, pk):
        participante = get_object_or_404(Participante, pk=pk)
        serializer = ParticipanteSerializer(participante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        participante = get_object_or_404(Participante, pk=pk)
        
        # Verifique se existem dependências ou registros relacionados antes de excluir
        # Exemplo: Presenças associadas ao participante, ou registros em outros modelos
        
        # Caso tenha dependências, trate ou remova as associações antes de excluir
        participante.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


