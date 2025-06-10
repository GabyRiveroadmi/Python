from django.db import models

class Cartera(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

class Billetera(models.Model):
    nombre = models.CharField(max_length=100)
    cuero = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cinto(models.Model):
    nombre = models.CharField(max_length=100)
    talle = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
