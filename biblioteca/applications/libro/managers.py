from django.db import models
from django.db.models import Q, Count


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

    def add_autor_libro(self, libro_id, autor_id):
        # .get(id=libro_id) // devuelve un solo registro
        libro = self.get(id=libro_id)
        # libro.<<relacion_many_to_many>>.add(objeto a añadir)
        libro.autores.add(autor_id)
        return libro

    def eliminar_autor_libro(self, libro_id, autor_id):
        # .get(id=libro_id) // devuelve un solo registro
        libro = self.get(id=libro_id)
        libro.objects.remove(autor_id)
        return libro

    def list_libros_cantidad_prestamos(self):
        # Devuelve un diccionario con los nombres especificados, util cuando se requier un valor
        # .aggregate // permite realizar agrupaciones y operaciones sobre relaciones
        return self.aggregate(
            numero_prestamos=Count('libro_prestamo')  # libro_prestamo => related_name en prestamo con libro
        )

    """
    Implementando trigram Postgresql

    // Permite separar en partes un valor para hacer un like %% super dotado
    // Solo funciona si el string es mayor a 3 de longitud

    \c nombre_bd
    CREATE EXTENSION pg_trgm;
    CREATE INDEX <<name_idx>> ON "<<name_app>>_<<name_model>>" USING GIN(<<name_field_to_search>> gin_trgm_ops);
    """

    def busqueda_titulo_libro_trigram(self, consulta):
        # __trigram_similar // usara la capacidad de postgres de trigram
        return self.filter(
            titulo__trigram_similar=consulta
        )


class CategoriaManager(models.Manager):
    """Managers para el modelo libro"""

    def listar_categorias_por_autor(self, id_autor):
        # categoria_libro__autores__id=id_autor // accede por el related name
        # categoria_libro > autores > por id
        # .distinct() // removera los registros repetidos
        return self.filter(
            categoria_libro__autores__id=id_autor
        ).distinct()

    def listar_categorias_cantidad_de_libros(self):
        # Retorna un queryset como valor añadido al queryset inicial del modelo,
        # util cuando se requiere recibir el objeto como tal, ya que iterara sobre cada registro del modelo
        # annotate => permite realizar agrupaciones y operaciones sobre relaciones

        return self.annotate(
            cantidad_libros=Count('categoria_libro')  # 'categoria_libro => related Name || nombre de la relacion
        )
