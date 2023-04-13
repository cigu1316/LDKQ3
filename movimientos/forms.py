from django import forms

from movimientos.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['date','descriptions', 'income', 'expenses','balance', ]
        
        

class FormularioSumaResta(forms.ModelForm):
    suma = forms.IntegerField()
    resta = forms.IntegerField()