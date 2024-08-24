from django.db import models

# Create your models here.

class MarcaModel(models.Model) :
    codigo = models.IntegerField(blank=True, null=True);
    nome = models.CharField(max_length=256,blank=True, null=True )

class CarroModeloModel(models.Model):
    codigoMarca = models.ForeignKey('MarcaModel', models.DO_NOTHING, blank=True, null=True)
    codigo = models.CharField(max_length=75)   
    nome = models.CharField(max_length=75)


