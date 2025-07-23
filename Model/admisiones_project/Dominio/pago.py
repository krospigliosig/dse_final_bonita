#!/usr/bin/python
# -*- coding: utf-8 -*-

class Pago:
	def __init__(self):
		self.id = None
		self.postulante_id = None
		self.monto = None
		self.moneda = None
		self.fecha_creacion = None
		self.estado = None
		self.transaccion_bancaria = None

	def aprobar(self, ):
		pass

	def rechazar(self, motivo):
		pass

	def es_aprobado(self, ):
		pass
