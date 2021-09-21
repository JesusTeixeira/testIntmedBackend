from polls.models import Consultas
from django.http.response import JsonResponse
from polls.models import Especialidade, Medicos
from django.shortcuts import HttpResponse


def listespecialidade(request):
    print(list(Especialidade.objects.all()))
    liste_specialidade = list(Especialidade.objects.all().values())
    
    return JsonResponse({"especialidade": liste_specialidade})



def listmedicos(request):
    print(list(Medicos.objects.all()))
    list_medicos = list(Medicos.objects.all().values())

    return JsonResponse({"medicos": list_medicos})



def listconsultas(request):
    print(list(Consultas.objects.all()))
    list_consultas = list(Consultas.objects.all().values())

    return JsonResponse({"consultas": list_consultas})