from django.urls import path
from . import views

# autores:<<name_path>>
urls_lector = ([
                  path(route='prestamos/add', view=views.RegistrarPrestamo.as_view(), name='prestamos_add'),
                  path(route='prestamos/error', view=views.ErrorCreacionPrestamoView.as_view(), name='prestamos_error'),
              ], 'prestamos')
