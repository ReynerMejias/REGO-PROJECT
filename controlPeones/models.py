from django.db import models
from django.utils import timezone

class Peon(models.Model):
    n_cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    peon = models.OneToOneField(Peon, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=timezone.now)
    cuota_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrato de {self.peon.nombre} ({self.fecha_inicio})"

class Retiro(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)    
    fecha_retiro = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Retiro de {self.monto} ({self.contrato.peon.nombre}, {self.fecha_retiro})"