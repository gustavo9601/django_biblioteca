from django.urls import path
from . import views

# autores:<<name_path>>
urls_autor = ([
                  path(route='', view=views.ListarAutores.as_view(), name='lista_autores'),
              ], 'autores')
