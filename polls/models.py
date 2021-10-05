from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime


class Especialidade(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=None)

    def __str__(self) -> str:
        return super().__str__()


class Medico(models.Model):
    crm = models.IntegerField(unique=True, blank=False, null=None)
    nome = models.CharField(max_length=255, blank=False, null=None) 
    especialidade = models.ForeignKey(Especialidade, on_delete=models.DO_NOTHING, null=True, default=None)
    email = models.EmailField(blank=False, null=True)
    telefone = models.PositiveIntegerField(null=True, blank=False)

    def __str__(self) -> str:
        return f'{self.crm} - {self.nome}'


class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(default=datetime.now())
    medico = models.ForeignKey(Medico, on_delete=CASCADE)

