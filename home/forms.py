from django import forms

class PersonaFormularios(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    
class BuequedaPersonaFormularios(forms.Form):
    nombre = forms.CharField(max_length=30,required=False)