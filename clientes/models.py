from django.db import models

# Create your models here.

class Adress(models.Model):
    city = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return 'Cidade:'+self.city+', bairro:'+self.neighborhood+', rua:'+self.street+', Nº'+self.house_number



class  Cliente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='clientes_fotos', null='TRUE')
    adress = models.OneToOneField(Adress, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
