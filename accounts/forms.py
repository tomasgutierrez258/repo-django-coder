from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.CharField(label='Usuario', max_length = 20)
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        help_text = {key: '' for key in fields} #es una forma de crear un diccionario dado las keys en lista y con valores en vacio (list comprehension)