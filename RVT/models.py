from django.db import models

class TipoElemento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Costo(models.Model):
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descripcion}: {self.valor} por {self.unidad.abreviatura or self.unidad.nombre}"

class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoElemento, on_delete=models.CASCADE)
    materiales = models.ManyToManyField(Material, blank=True)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.ForeignKey(Costo, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='elementos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

#Aqui creo mis MERs 

# Create your models here.
