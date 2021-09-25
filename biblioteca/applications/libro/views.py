from django.views.generic import ListView, DetailView

# Local Apps
from .models import Libro


# Create your views here.
class ListarLibros(ListView):
    model = Libro
    context_object_name = 'libros'
    template_name = 'libro/listar.html'

    def get_queryset(self):
        # obteniendo el parametro por GET
        consulta = self.request.GET.get('consulta', '')
        fecha_inicio = self.request.GET.get('fecha_inicio', '2000-01-01')
        fecha_fin = self.request.GET.get('fecha_fin', '2000-01-01')

        print('fecha_inicio', fecha_inicio)
        print('fecha_fin', fecha_fin)

        # listar_autores() // funcion dentro del manager
        # return Autor.objects.listar_autores()

        # buscar_autor(param) // funcion dentro del manager
        return Libro.objects.listar_libros_por_fechas(consulta, fecha_inicio, fecha_fin)


class ListarLibros2(ListView):
    model = Libro
    context_object_name = 'libros'
    template_name = 'libro/listar2.html'

    def get_queryset(self):
        id_categoria = self.kwargs['id_categoria']
        return Libro.objects.listar_libros_por_categoria(id_categoria)


class LibroDetalle(DetailView):
    model = Libro
    context_object_name = 'libro'
    template_name = 'libro/detalle.html'