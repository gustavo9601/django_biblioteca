from django.db import models
from django.db.models import Q


class LibroManager(models.Manager):
    """Managers para el modelo libro"""

    def listar_libros(self, consulta):
        # fecha__range=('2000-01-01', '2021-12-31') => between ('2000-01-01', '2021-12-31')
        return self.filter(
            titulo__icontains=consulta,
            fecha_publicacion__range=('2000-01-01', '2021-12-31')
        )

    def listar_libros_por_fechas(self, consulta, fecha_inicio, fecha_fin):
        # fecha__range=('2000-01-01', '2021-12-31') => between ('2000-01-01', '2021-12-31')
        return self.filter(
            titulo__icontains=consulta,
            fecha_publicacion__range=(fecha_inicio, fecha_fin)
        )

    def listar_libros_por_categoria(self, id_categoria):
        # categoria__id => relacion foreign key libro con categoria
        return self.filter(
            categoria__id=id_categoria
        ).order_by('titulo')


class CategoriaManager(models.Manager):
    """Managers para el modelo libro"""

    def listar_categorias_por_autor(self, id_autor):
        # categoria_libro__autores__id=id_autor // accede por el related name
        # categoria_libro > autores > por id
        # .distinct() // removera los registros repetidos
        return self.filter(
            categoria_libro__autores__id=id_autor
        ).distinct()
