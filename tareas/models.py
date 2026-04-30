from django.db import models


# Creas una clase que hereda de models.Model
class Tarea(models.Model): 
    # Definimos los campos (columnas de la tabla)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Un método especial para que al ver la tarea, tenga un nombre bonito
    def __str__(self):
        return self.titulo