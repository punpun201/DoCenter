from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    apellido = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    contraseña = models.CharField(max_length=100, null=True, blank=True) 
    telefono = models.IntegerField(null=True, blank=True)
    RFC = models.CharField(max_length=250, null=True, blank=True)
    CURP = models.CharField(max_length=250, null=True, blank=True)
    curriculum = models.CharField(max_length=250, null=True, blank=True)
    constancia_fiscal = models.CharField(max_length=250, null=True, blank=True)
    certificado_academico = models.CharField(max_length=250, null=True, blank=True)
    rol = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"