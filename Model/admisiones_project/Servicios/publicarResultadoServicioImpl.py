from Dominio.resultadoExamen import ResultadoExamen
from Repositorio.Django.resultadoRespositorioImpl import ResultadoRepositorioImpl

class PublicarResultadoServicioImpl:
    def __init__(self):
        self.repositorio = ResultadoRepositorioImpl()

    def publicar(self, postulante_id, puntaje, aprobado, comentario=""):
        resultado = ResultadoExamen(postulante_id, puntaje, aprobado, comentario)
        return self.repositorio.guardar(resultado)