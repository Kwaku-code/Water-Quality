from django.db import models
from django.db.models.fields import FloatField, IntegerField, CharField

# Create your models here.
class Variables(models.Model):
    ph = models.FloatField(default=0.0)
    Hardness = models.FloatField(default=0.0)
    Solids = models.FloatField(default=0.0)
    Chloramines = models.FloatField(default=0.0)
    Sulfate = models.FloatField(default=0.0)
    Conductivity = models.FloatField(default=0.0)
    Organic_carbon = models.FloatField(default=0.0)
    Trihalomethanes = models.FloatField(default=0.0)
    Turbidity = models.FloatField(default=0.0)
    Potability = models.CharField(max_length=20)

