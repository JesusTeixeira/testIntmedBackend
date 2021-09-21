from django.db import models
from django.db.models.deletion import CASCADE

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)


class Medicos(models.Model):
    crm = models.IntegerField(default=0)
    nome_medico = models.CharField(max_length=50) 
    especialidade_medico = models.ForeignKey(Especialidade, on_delete=models.DO_NOTHING)

class Consultas(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField()
    medico = models.ForeignKey(Medicos, on_delete=CASCADE)