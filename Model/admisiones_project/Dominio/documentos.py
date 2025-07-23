#!/usr/bin/python
# -*- coding: utf-8 -*-

class Documentos:
	def __init__(self):
		self.id = None
		self.nombre_archivo = None
		self.fecha_carga = None
		self.estado = None

	def es_formato_valido(self, ):
		return self.nombre_archivo.endswith('.pdf') or self.nombre_archivo.endswith('.jpg') or self.nombre_archivo.endswith('.png')	
