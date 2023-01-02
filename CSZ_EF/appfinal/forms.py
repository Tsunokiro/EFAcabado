from django import forms
from .models import Producto, Curso

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields='__all__'