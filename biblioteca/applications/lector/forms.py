from django import forms
from .models import Prestamo

from applications.libro.models import Libro

class PrestamoFormulario(forms.ModelForm):
    class Meta:
        # Conectamos el formulario con un modelo
        model = Prestamo

        # Especifica que campos se administraran desde el formulario
        fields = ('lector', 'libro')


class PrestamoMultipleLibrosFormulario(forms.ModelForm):

    # Creando un campo manualmnete, multiple
    libros = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        # Conectamos el formulario con un modelo
        model = Prestamo

        # Especifica que campos se administraran desde el formulario
        fields = (
            'lector',
        )


    def __init__(self, *args, **kwargs):
        super(PrestamoMultipleLibrosFormulario, self).__init__(*args, **kwargs)
        # inicializa los datos que confirmaran el queryset del ModelMultipleChoiceField
        self.fields['libros'].queryset = Libro.objects.all()
