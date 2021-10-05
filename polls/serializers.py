from django.db.models import fields
from polls.models import Medico, Especialidade, Consulta
from rest_framework import serializers
from rest_framework import permissions


owner = serializers.ReadOnlyField(source='owner.username')

class EspecialidadeSerializar(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id','nome']

class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializar(many=False, read_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'email', 'telefone', 'especialidade']

class ConsultaSerializar(serializers.ModelSerializer):
    medico = MedicoSerializer(many=False, read_only=True)

    class Meta:
        model = Consulta
        fields =  ['id', 'medico', 'dia', 'horario']