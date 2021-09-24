from django.shortcuts import render
from django.views.generic import ListView

# Local Apps
from .models import Autor


# Create your views here.
class ListarAutores(ListView):
    model = Autor
    context_object_name = 'autores'
    template_name = 'autor/listar.html'

    def get_queryset(self):
        # obteniendo el parametro por GET
        consulta = self.request.GET.get('consulta', '')

        # listar_autores() // funcion dentro del manager
        # return Autor.objects.listar_autores()

        # buscar_autor(param) // funcion dentro del manager
        return Autor.objects.buscar_autor_4(consulta=consulta)
