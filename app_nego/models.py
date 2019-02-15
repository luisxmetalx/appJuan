from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.pk, self.codigo, self.nombre,self.descripcion, self.cantidad)
