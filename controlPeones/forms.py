from django import forms
from django.forms import ModelForm
from .models import Peon, Contrato, Retiro

class PeonForm(ModelForm):
    n_cedula = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Peon
        fields = '__all__'
        exclude = ['activo']

class ContratoForm(ModelForm):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',  'type': 'date'}))
    cuota_mensual = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control dinero', 'type': 'number'}))
    class Meta:
        model = Contrato
        fields = '__all__'  
        exclude = ['peon']

class RetiroForm(ModelForm):
    fecha_retiro = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',  'type': 'date', 'id': 'fechaFinal'}))
    monto = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control dinero', 'type': 'number', 'id': 'resultado'}))
    class Meta:
        model = Retiro
        fields = '__all__'
        exclude = ['contrato']