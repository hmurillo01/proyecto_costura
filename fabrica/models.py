from django.db import models

# Create your models here.
# En tu archivo models.py

# Tabla fabrica
class Fabrica(models.Model):
    nit = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    id_costura = models.ForeignKey('Costureras', on_delete=models.CASCADE)

# Tabla costureras
class Costureras(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)

# Tabla Estado, es el estado que va tener las tareas
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

# Tabla Tareas
class Tareas(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    cant_prendas = models.IntegerField()
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    id_estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    id_fabrica = models.ForeignKey('Fabrica', on_delete=models.CASCADE)
    id_costurera = models.ForeignKey('Costureras', on_delete=models.SET_NULL, null=True, blank=True)
