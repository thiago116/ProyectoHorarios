from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    is_coordinador = widgets.CheckboxInput(
        attrs={
            "class":"form-control"
        }
    )

    class Meta:
        model = Usuario
        fields = ('username','password1','password2','is_instructor','is_coordinador','is_JGrupo')

class AddFichas(forms.ModelForm):
    class Meta:
        model = Fichas
        fields = ['programa_de_formacion','numero','jefe_ficha','jornada_de_ficha','fecha_inicio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['programa_de_formacion'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['numero'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['jefe_ficha'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['jornada_de_ficha'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['fecha_inicio'].widget.attrs.update({
            'class': 'form-control',
            'type':'date'
        })
class AddInstructores(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['nombre','apellidos','tipo_instructor']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['apellidos'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['tipo_instructor'].widget.attrs.update({
            'class':'form-control'
        })


    '''numero = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    programa_de_formacion = forms.CharField(
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control"
            }
        )
    )'''


