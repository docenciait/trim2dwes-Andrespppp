from django.db import models

# Create your models here.

class Denuncia(models.Model):
    id = models.AutoField(primary_key=True)
    # usuario = models.ForeignKey(D)
    titulo = models.CharField(max_length=255)
    descripcion =  models.TextField()
    # imagen ImageField
    categoria = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    # fecha_creacion= models.AutoFieldDataTimeField

    def __str__(self):
        return str(self.id) + ' - ' + self.name