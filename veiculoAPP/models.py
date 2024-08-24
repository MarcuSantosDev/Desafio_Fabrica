from django.db import models

# Create your models here.

class MarcaModel(models.Model) :
    codigo = models.IntegerField(blank=True, null=True);
    nome = models.CharField(max_length=256,blank=True, null=True )

    