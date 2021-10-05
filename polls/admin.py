from django.contrib import admin
from .models import Consulta, Especialidade, Medico


admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Consulta)