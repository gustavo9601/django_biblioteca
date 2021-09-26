from datetime import date

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import Prestamo
from .forms import PrestamoFormulario


# Create your views here.
class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    # Asociando el formulario que controla el modelo
    form_class = PrestamoFormulario

    success_url = reverse_lazy('prestamos:prestamos_add')

    def form_valid(self, formulario):
        print("*" * 15)
        print("Data del formulario:")
        print(type(formulario.cleaned_data))
        print(formulario.cleaned_data)

        # 1. Forma de crear
        # formulario.cleaned_data['lector'] // accede a los valores que pasaron las validaciones
        """Prestamo.objects.create(
            lector=formulario.cleaned_data['lector'],
            libro=formulario.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )"""

        # 2. Forma
        # Es usada tambien para actualizar datos
        """prestamo = Prestamo(
            lector=formulario.cleaned_data['lector'],
            libro=formulario.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )"""

        # 3. Forma
        # Es usada tambien para actualizar datos, usando unicamente los campos validados
        prestamo = Prestamo(
            **formulario.cleaned_data,
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        # Actualizando el stock del libro
        libro = formulario.cleaned_data['libro']
        print("type libro ", type(libro))
        libro.stock = libro.stock - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(formulario)


class RegistrarPrestamoForma2(FormView):
    template_name = 'lector/add_prestamo.html'
    # Asociando el formulario que controla el modelo
    form_class = PrestamoFormulario

    success_url = reverse_lazy('prestamos:prestamos_add')

    def form_valid(self, formulario):
        print("*" * 15)
        print("Data del formulario:")
        print(type(formulario.cleaned_data))
        print(formulario.cleaned_data)

        obj, is_created = Prestamo.objects.get_or_create(
            # Valores de condicion para tratar de encontrar el registro
            lector=formulario.cleaned_data['lector'],
            libro=formulario.cleaned_data['libro'],
            devuelto=False,
            # si no se encuentra el registro los valores a autocompletar
            defaults={
                'fecha_prestamo': date.today()
            }
        )

        if is_created:
            # Actualizando el stock del libro
            libro = formulario.cleaned_data['libro']
            print("type libro ", type(libro))
            libro.stock = libro.stock - 1
            libro.save()
            return super(RegistrarPrestamoForma2, self).form_valid(formulario)
        else:
            return HttpResponseRedirect(reverse_lazy('prestamos:prestamos_error'))


class ErrorCreacionPrestamoView(TemplateView):
    template_name = 'error.html'