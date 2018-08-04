from django.forms import ModelForm
from .models import Cliente, Adress


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'age','photo','adress']


class AdressForm(ModelForm):
    class Meta:
        model = Adress
        fields = ['city', 'neighborhood', 'street', 'house_number']



