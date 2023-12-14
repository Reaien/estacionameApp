from django import forms


class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    password = forms.CharField(max_length=12)
    email = forms.CharField(max_length=100)
    edad = forms.CharField(max_length=100)
    comuna = forms.CharField(max_length=100)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class EstacionamientoForm(forms.Form):
    nombreContacto = forms.CharField(max_length=50)
    fonoContacto = forms.CharField(max_length=15)
    nombreComuna = forms.CharField(max_length=25)
    direccion = forms.CharField(max_length=90)
    imagenEstacionamiento = forms.FileField()