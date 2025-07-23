from django.db import models

# Create your models here.
class Postulante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"