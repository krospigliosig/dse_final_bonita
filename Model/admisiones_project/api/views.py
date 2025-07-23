from django.shortcuts import render

from rest_framework import viewsets
from .models import Postulante
from .serializers import PostulanteSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Servicios.publicarResultadoServicioImpl import PublicarResultadoServicioImpl

class PostulanteViewSet(viewsets.ModelViewSet):
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer
    
@api_view(['POST'])
def publicar_resultado(request):
    data = request.data
    postulante_id = data.get("postulante_id")
    puntaje = float(data.get("puntaje"))
    aprobado = data.get("aprobado") in ["true", "True", True]
    comentario = data.get("comentario", "")

    servicio = PublicarResultadoServicioImpl()
    resultado = servicio.publicar(postulante_id, puntaje, aprobado, comentario)

    return Response({
        "id": resultado.id,
        "postulante_id": resultado.postulante_id,
        "puntaje": resultado.puntaje,
        "aprobado": resultado.aprobado,
        "fecha_publicacion": str(resultado.fecha_publicacion),
        "comentario": resultado.comentario
    })
    
    
@api_view(['POST'])
def validar_documentos(request):
    data = request.data
    postulante_id = data.get("postulante_id")
    
    documentos_validados = True
    estado = "DOCUMENTOS_VALIDOS"

    return Response({
        "postulante_id": postulante_id,
        "documentos_validados": documentos_validados,
        "estado": estado
    })