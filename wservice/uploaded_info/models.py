from django.db import models

# Create your models here.
class Posteo(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha}: {self.contenido[:50]}"