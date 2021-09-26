from django import forms
from .models import Prestamo


class PrestamoFormulario(forms.ModelForm):
    class Meta:
        # Conectamos el formulario con un modelo
        model = Prestamo

        # Especifica que campos se administraran desde el formulario
        fields = ('lector', 'libro')
