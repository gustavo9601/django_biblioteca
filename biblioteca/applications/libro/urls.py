from django.urls import path
from . import views

# autores:<<name_path>>
urls_libro = ([
                  path(route='libros/', view=views.ListarLibros.as_view(), name='lista_libros'),
                  path(route='libros-por-categoria/<int:id_categoria>', view=views.ListarLibros2.as_view(),
                       name='lista_libros'),
                  path(route='libro-detalle/<int:pk>', view=views.LibroDetalle.as_view(), name='libro_detalle'),
              ], 'libros')
