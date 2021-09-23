from django.db import models
from applications.libro.models import Libro


# Create your models here.
# Create your models here.
class Lector(models.Model):
    nombres = models.CharField('Nombres', max_length=30)
    apellidos = models.CharField('Apellidos', max_length=30)
    nacionalidad = models.CharField('Nacionalidad', max_length=30)
    edad = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'lectores'

    def __str__(self):
        return f"{self.nombres} | {self.apellidos}"


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField('Fecha de prestamo')
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField('Ya se devolivio?', default=False)

    class Meta:
        db_table = 'prestamos'

    def __str__(self):
        return f"{self.libro.titulo} | {self.lector.nombres}"