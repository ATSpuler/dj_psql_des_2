from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    
    # to do
    #implementar una relacion a Tareas
  








# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

# equivalent to
"""
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
"""
"""
tipos de datos para asignar a las propiedades del modelo
- CharField
- TextField
- IntegerField
- DateField
- EmailField
- AutoField
- ForeignKEy
- ManyToManyField
- BooleanField
"""

# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)

# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
    
    # Album contiene una clave foranea hacia el modelo Musician.



































#from django.db import models

# class Gen(models.Model):
#     campo1 = models.CharField(max_length=50)
#     valor = models.IntegerField()

# class Persona(models.Model):
#     id = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     correo = models.EmailField(max_length=50)

