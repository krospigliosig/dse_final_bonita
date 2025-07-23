#!/usr/bin/python
# -*- coding: utf-8 -*-

class Postulante:
	def __init__(self):
		self.id = None
		self.nombres = None
		self.apellidos = None
		self.dni = None
		self.email = None
		self.fecha_nacimiento = None
		self.documentos = None
		self.estado = None

	def agregar_documentos(self, doc):
		pass

	def quitar_documentos(self, doc_id):
		pass

	def actualizar_datos(self, dto):
		pass

	def documentos_validos(self):
		return all(doc.es_formato_valido() for doc in self.documentos)
