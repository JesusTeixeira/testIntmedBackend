from django.contrib import admin
from .models import Consultas, Especialidade, Medicos


admin.site.register(Especialidade)
admin.site.register(Medicos)
admin.site.register(Consultas)