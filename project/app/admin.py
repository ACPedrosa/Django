from django.contrib import admin
from .models import Usuario, Participante, Colaborador, Atividade, Turma

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Participante)
admin.site.register(Colaborador)
admin.site.register(Atividade)
admin.site.register(Turma)