from rest_framework import views, viewsets
from rest_framework import permissions
from polls.serializers import MedicoSerializer, EspecialidadeSerializar, ConsultaSerializar
from polls.models import Consulta, Especialidade, Medico
from polls.permissions import IsOwnerOrReadOnly



permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class MedicoViewSet(viewsets.ModelViewSet):
 
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.IsAuthenticated]


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializar
    permission_classes = [permissions.IsAuthenticated]


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializar
    permission_classes = [permissions.IsAuthenticated]

