from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    descripcion = models.CharField('Descripcion', max_length=50, null=True, blank=True)

    objects = CategoriaManager()

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.descripcion}"


class Libro(models.Model):
    titulo = models.CharField('Titulo', max_length=30)
    fecha_publicacion = models.DateField('Fecha publicacion')
    portada = models.ImageField(upload_to='portadas')
    visitas = models.PositiveIntegerField('Visitas')

    # related_name='categoria_libro' => relacion inversa y nombre para acceder desde el manager o el objects
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)

    objects = LibroManager()

    class Meta:
        db_table = 'libros'

    def __str__(self):
        return f"{self.id} | {self.titulo} | {self.fecha_publicacion}"


"""
Implementando trigram Postgresql
// Permite separar en partes un valor para hacer un like %% super dotado

\c nombre_bd
CREATE EXTENSION pg_trgm;
CREATE INDEX <<name_idx>> ON "<<name_app>>_<<name_model>>" USING GIN(<<name_field_to_search>> gin_trgm_ops);
"""
