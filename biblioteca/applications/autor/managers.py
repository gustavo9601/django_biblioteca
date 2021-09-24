from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):
    """Managers para el modelo autor"""

    def listar_autores(self):
        # self.all() => Autor.objects.all()
        return self.all()

    def buscar_autor(self, consulta: str):
        # __incontains => %param%
        return self.filter(
            nombre__icontains=consulta
        )

    def buscar_autor_2(self, consulta: str):
        # __incontains => %param%
        #   Q(nombre__icontains=consulta) | Q(apellidos__icontains=consulta) => condition OR || AND condition ( | & )
        return self.filter(
            Q(nombre__icontains=consulta) | Q(apellidos__icontains=consulta)
        )

    def buscar_autor_3(self, consulta: str):
        # __incontains => %param%
        # .exclude(edad=35) => edad != 35
        # .exclude(Q(nombre__icontains=consulta) | Q(apellidos__icontains=consulta)) => condition OR || AND condition ( | & )
        return self.filter(
            nombre__icontains=consulta
        ).exclude(edad=35).filter(apellidos__icontains=consulta)

    def buscar_autor_4(self, consulta: str):
        """
          edad__gt=40,  __gt => edad > 40
          edad__lt=65   __lt => edad < 65
          order_by(<<field>>, <<field_2>>)  => order by <<field>>
        """
        return self.filter(
            edad__gt=40,
            edad__lt=65
        ).order_by('apellidos')
