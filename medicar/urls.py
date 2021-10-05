
from django.contrib import admin
from django.urls import path, include
from polls import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'medicos', views.MedicoViewSet)
router.register(r'especialidades', views.EspecialidadeViewSet)
router.register(r'consultas', views.ConsultaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
