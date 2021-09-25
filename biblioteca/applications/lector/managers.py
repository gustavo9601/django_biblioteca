from django.db import models
from django.db.models import Q, Count, Avg, Sum


class PrestamoManager(models.Manager):
    """Managers para el modelo Prestamo"""

    def promedio_de_edades_lectores_libros(self, libro_id):
        return self.filter(
            libro__id=libro_id  # filta por la relacion con el libro
        ).aggregate(  # retorna un diccionario solo con los campos definidos como parametro
            promedio_edad=Avg('lector__edad'),  # devolvera el promedio por la relacion lector.edad
            suma_edad=Sum('lector__edad')  # devolvera la sumatoria de la edad
        )

    def cantidad_de_prestamos_por_libro(self):
        # values => group by libro | annotate => hace las operaciones de agregacion
        return self.values(
            'libro' # libro => nombre de relacion
        ).annotate(
            cantidad_prestamos=Count('libro')  # libro => nombre de relacion
        )
