from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

# Modelo para Usuário
class Usuario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Oculto'),
    ]

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)  # Remover o unique=True
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    senha = models.CharField(max_length=12, unique=True)  # Adiciona o campo de senha
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cidade = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    alergias = models.TextField(blank=True, null=True)
    descricao = models.TextField()  # Usar TextField para descrições mais longas

    def __str__(self):
        return self.nome
    
    def clean(self):
        super().clean()
        # Validação de CPF (com ou sem pontos e hífen)
        if self.cpf:
            # Remove qualquer caractere não numérico
            cpf = re.sub(r'\D', '', self.cpf)  
            if len(cpf) != 11:
                raise ValidationError("O CPF deve ter 11 dígitos.")
            
            # Verifica a validade do CPF
            if not re.match(r'^\d{11}$', cpf):  # Verifica apenas os 11 dígitos numéricos
                raise ValidationError("O CPF não é válido.")

# Modelo para Participante
class Participante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Participante: {self.usuario.nome}"

# Modelo para Colaborador
class Colaborador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)  # Chave estrangeira para Usuario
    codColaborador = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"Colaborador: {self.usuario.nome}"

# Modelo para Atividade
class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()
    profissional_responsavel = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

# Modelo para Turma
class Turma(models.Model):
    nome = models.CharField(max_length=255)
    horario_inicio = models.TimeField()  # Para hora de início
    horario_fim = models.TimeField()  # Para hora de término
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Participante, through='Presenca')

    def __str__(self):
        return self.nome

# Modelo para Presença
class Presenca(models.Model):
    aluno = models.ForeignKey(Participante, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_presenca = models.DateField(default=timezone.now)
    presenca = models.BooleanField(default=False)

    def marcar_presenca(self):
        self.presenca = True
        self.save()

    def clean(self):
        if self.data_presenca > timezone.now().date():
            raise ValidationError("A data de presença não pode ser no futuro.")

    def __str__(self):
        return f"{self.aluno.usuario.nome} - {self.turma.nome} - {self.data_presenca}"

# Modelo para Certificado
class Certificado(models.Model):
    aluno = models.ForeignKey(Participante, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    data_emissao = models.DateField(auto_now_add=True)
    horas_participacao = models.PositiveIntegerField()

    def __str__(self):
        return f"Certificado de {self.aluno.usuario.nome} para {self.atividade.nome}"

# Modelo para Histórico
class Historico(models.Model):
    aluno = models.ForeignKey(Participante, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='historicos')
    presenca = models.ForeignKey(Presenca, on_delete=models.SET_NULL, null=True, blank=True)  # Chave estrangeira para Presenca
    data_atividade = models.DateField(default=timezone.now)  # Data em que a atividade foi realizada
    certificado = models.ForeignKey(Certificado, on_delete=models.SET_NULL, null=True, blank=True)  # Certificado gerado, se houver

    def __str__(self):
        return f"{self.aluno.usuario.nome} - {self.atividade.nome} - {self.data_atividade}"

    class Meta:
        verbose_name = "Histórico"
        verbose_name_plural = "Históricos"
