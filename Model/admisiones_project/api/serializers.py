from rest_framework import serializers
from .models import Postulante

from Dominio.resultadoExamen import ResultadoExamen

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = '__all__'


class ResultadoExamenSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    postulante_id = serializers.UUIDField()
    puntaje = serializers.FloatField()
    aprobado = serializers.BooleanField()
    fecha_publicacion = serializers.DateTimeField()
    comentario = serializers.CharField()