from .models import Usuario, Participante, Colaborador, Atividade, Turma
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'cpf', 'sexo', 'senha']
        extra_kwargs = {
            'senha': {'write_only': True}  # A senha será write-only
        }

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está cadastrado.")
        return value

    def validate_senha(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value

class ParticipanteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Participante
        fields = ['usuario']  # Incluindo apenas a chave estrangeira do Usuario

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        participante = Participante.objects.create(usuario=usuario)
        return participante

#Serializers do Colaborador
class ColaboradorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Colaborador
        fields = ['usuario'] # Incluindo apenas a chave estrangeira do Usuario

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        colaborador = Colaborador.objects.create(usuario=usuario)
        return colaborador

#Serializers da Turma
class TurmaSerializer(serializers.ModelSerializer):
    atividade = serializers.PrimaryKeyRelatedField(queryset=Atividade.objects.filter(status=True))
    alunos = serializers.StringRelatedField(many=True, read_only=True)  # Retorna uma lista de alunos por nome (opcional).

    class Meta:
        model = Turma
        fields = ['id', 'nome', 'horario_inicio', 'horario_fim', 'atividade', 'alunos']
        read_only_fields = ['id', 'alunos']  # Evita que 'id' e 'alunos' sejam escritos.

    def validate(self, data):
        # Verifica se o horário de início é anterior ao horário de término
        if data['horario_inicio'] >= data['horario_fim']:
            raise serializers.ValidationError("O horário de início deve ser antes do horário de término.")
        return data

    def create(self, validated_data):
        # Criação da turma
        return Turma.objects.create(**validated_data)


#Serializers da Atividade
class AtividadeSerializer(serializers.ModelSerializer):
    profissional_responsavel = serializers.PrimaryKeyRelatedField(queryset=Colaborador.objects.all())
    turmas = TurmaSerializer(many=True, read_only=True, source='turma_set')  # Exibe as turmas vinculadas.

    class Meta:
        model = Atividade
        fields = [
            'id',
            'nome',
            'descricao',
            'carga_horaria',
            'profissional_responsavel',
            'status',
            'turmas',
        ]
        read_only_fields = ['id', 'turmas']  # Evita escrita em campos read-only.

    def validate_carga_horaria(self, value):
        # Garante que a carga horária seja positiva
        if value <= 0:
            raise serializers.ValidationError("A carga horária deve ser maior que zero.")
        return value

    def validate(self, data):
        # Validações adicionais (opcional)
        if not data.get('status', False):
            raise serializers.ValidationError("A atividade deve estar ativa para ser criada.")
        return data

    def create(self, validated_data):
        # Criação da atividade
        return Atividade.objects.create(**validated_data)



