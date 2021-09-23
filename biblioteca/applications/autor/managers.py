from django.db import models

class AutorManager(models.Manager):
    """Managers para el modelo autor"""

    def listar_autores(self):
        # self.all() => Autor.objects.all()
        return self.all()