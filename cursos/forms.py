from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'cols': 100}))