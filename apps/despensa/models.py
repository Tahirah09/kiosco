from django.db import models

class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=100)
  precio = models.FloatField()
  stock = models.IntegerField()
  categoria_producto = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.nombre}.{self.descripcion}"


class Categoria(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=100)
  producto = models.ForeignKey(Producto, on_delete= models.CASCADE)

  def __str__(self):
    return f"{self.nombre}.{self.descripcion}"
