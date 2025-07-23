from rest_framework.routers import DefaultRouter
from .views import PostulanteViewSet, publicar_resultado, validar_documentos
from django.urls import path, include

router = DefaultRouter()
router.register(r'postulantes', PostulanteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  
    path('resultados/', publicar_resultado, name='publicar_resultado'),
    path('api/postulantes/validar-documentos/', validar_documentos, name= 'validar_documentos'),
]