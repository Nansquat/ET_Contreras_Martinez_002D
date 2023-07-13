from django import forms
from .models import Planta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = [ 'codigo', 'tipo', 'ambiente','garantia' , 'categoria', 'imagen']
        labels = {
            'codigo' : 'Codigo',
            'tipo' : 'Tipo',
            'ambiente' : 'Ambiente',
            'garantia' : 'Garantia',
            'categoria' : 'Categoria',
            'imagen' : 'Imagen'
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo..',
                    'id' : 'codigo',
                    'class' : 'form-control'
                }
            ),
            'tipo' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese tipo de producto..',
                    'id' : 'tipo',
                    'class' : 'form-control'
                }
            ),
            'ambiente' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese ambiente de producto..',
                    'id' : 'ambiente',
                    'class' : 'form-control'
                }
            ),
            'garantia' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese garantía de producto..',
                    'id' : 'garantia',
                    'class' : 'form-control'
                }
            ),
            'categoria' : forms.Select(
                attrs={
                    'id' : 'categoria',
                    'class' : 'form-control'
                }
            ),
            'imagen' : forms.FileInput(
                attrs={
                    'id' : 'imagen',
                    'class' : 'form-control'
                }
            ) 
        }