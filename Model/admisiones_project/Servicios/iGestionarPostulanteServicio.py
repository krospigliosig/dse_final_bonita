#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class IGestionarPostulanteServicio(ABC):

    @abstractmethod
    def crear_postulante(self, data: dict):
        """
        Método que define la creación de un postulante.
        Recibe un diccionario con los datos necesarios.
        """
        pass