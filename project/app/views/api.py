from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Participante, Colaborador, Atividade, Turma
from app.serializers import ParticipanteSerializer, ColaboradorSerializer, AtividadeSerializer, TurmaSerializer
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
    
#CRUD colaborador
class ColaboradorView(APIView):
    """
    View para criar ou listar colaboradores.
    """

    def get(self, request):
        colaboradores = Colaborador.objects.all()
        serializer = ColaboradorSerializer(colaboradores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ColaboradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColaboradorDetailView(APIView):
    """
    View para recuperar, atualizar ou deletar um colaborador específico.
    """

    def get(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        serializer = ColaboradorSerializer(colaborador)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        serializer = ColaboradorSerializer(colaborador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        colaborador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#CRUD Atividade
class AtividadeView(APIView):
    """
    View para criar ou listar atividades.
    """

    def get(self, request):
        atividades = Atividade.objects.all()
        serializer = AtividadeSerializer(atividades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AtividadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AtividadeDetailView(APIView):
    """
    View para recuperar, atualizar ou deletar uma atividade específica.
    """

    def get(self, request, pk):
        atividade = get_object_or_404(Atividade, pk=pk)
        serializer = AtividadeSerializer(atividade)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        atividade = get_object_or_404(Atividade, pk=pk)
        serializer = AtividadeSerializer(atividade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        atividade = get_object_or_404(Atividade, pk=pk)
        atividade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CRUD Turmas

class TurmaView(APIView):
    """
    View para criar ou listar turmas.
    """

    def get(self, request):
        turmas = Turma.objects.all()
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TurmaDetailView(APIView):
    """
    View para recuperar, atualizar ou deletar uma turma específica.
    """

    def get(self, request, pk):
        turma = get_object_or_404(Turma, pk=pk)
        serializer = TurmaSerializer(turma)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        turma = get_object_or_404(Turma, pk=pk)
        serializer = TurmaSerializer(turma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        turma = get_object_or_404(Turma, pk=pk)
        turma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

