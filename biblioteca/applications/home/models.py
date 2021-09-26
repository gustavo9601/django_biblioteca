from django.db import models


# Create your models here.
class Home(models.Model):
    titulo = models.CharField('nombres', max_length=50)
    pais = models.CharField('pais', max_length=50)
    pais_secundario = models.CharField('pais secundario', max_length=50, null=True, blank=True)
    edad = models.IntegerField('edad')


    class Meta:
        verbose_name = 'Inicio'
        verbose_name_plural = 'Inicios'
        db_table = 'homes'
        # unique_together => verifica que no pueden tener el mismo valor al insertar
        unique_together = ['pais', 'pais_secundario']
        # permite crear restrincciones sobre los campos
        # models.CheckConstraint(check=models.Q(<<validation_field>>), name='<<name_validation_if_Error_Exists>>')
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]



    def __str__(self):
        return f"{self.titulo} | {self.pais} | {self.edad}"

# Heredando desde un modelo existente
class Pagina1(Home):
    url = models.CharField('url', max_length=50)

# Creando un modelo, pero abstractacto
# De esta forma servira como esquema para otros pero no se creara en la BD
class Pagina(models.Model):
    url = models.CharField('url', max_length=50)
    navigation = models.BooleanField(default=False)

    class Meta:
        abstract = True

# Heredando desde un modelo existente
class Pagina2(Pagina):
    cuerpo_pagina = models.CharField('Cuerpo de la pagina', max_length=500)