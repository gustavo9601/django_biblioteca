from django.db import models
from applications.autor.models import Autor


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    descripcion = models.CharField('Descripcion', max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return f"{self.nombre} | {self.descripcion}"


class Libro(models.Model):
    titulo = models.CharField('Titulo', max_length=30)
    fecha_publicacion = models.DateField('Fecha publicacion')
    portada = models.ImageField(upload_to='portadas')
    visitas = models.PositiveIntegerField('Visitas')

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)

    class Meta:
        db_table = 'libros'

    def __str__(self):
        return f"{self.titulo} | {self.fecha_publicacion}"
