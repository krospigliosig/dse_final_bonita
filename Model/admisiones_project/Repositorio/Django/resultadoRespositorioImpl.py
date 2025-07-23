#!/usr/bin/python
# -*- coding: utf-8 -*-

from Dominio.resultadoRepositorio import ResultadoRepositorio
from Dominio.resultadoExamen import ResultadoExamen  # Add this import if ResultadoExamen is defined in this module


class ResultadoRepositorioImpl:
    def __init__(self):
        self.resultados = []

    def guardar(self, resultado: ResultadoExamen):
        self.resultados.append(resultado)
        return resultado

    def obtener_todos(self):
        return self.resultados