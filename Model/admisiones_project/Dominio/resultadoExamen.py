#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import uuid

class ResultadoExamen:
    
    def __init__(self, postulante_id, puntaje, aprobado=False, comentario=""):
        self.id = str(uuid.uuid4())
        self.postulante_id = postulante_id
        self.puntaje = puntaje
        self.aprobado = aprobado
        self.fecha_publicacion = datetime.now()
        self.comentario = comentario

    def Operation1(self, ):
        pass

    def es_aprobado(self, ):
        pass
