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

# class Potability(models.Model):
#     level = models.IntegerField(default=0.0)
#     input_var = models.ForeignKey(IndependentVariables, on_delete = models.CASCADE)
    

# class SignUp(models.Model):
#     username = models.CharField(max_length=200, unique=True)
#     password = models.CharField(max_length=200, unique=True)

#     def __str__(self):
#         return f"level={self.username},{self.password}"

# class Login(models.Model):
#     username = models.CharField(max_length=200, unique=True)
#     password = models.CharField(max_length=200, unique=True)

#     def __str__(self):
#         return f"level={self.username},{self.password}"

# class EnterVariables(models.Model):
#     ph = models.FloatField(default=0.0)
#     Hardness = models.FloatField(default=0.0)
#     Solids = models.FloatField(default=0.0)
#     Chloramines = models.FloatField(default=0.0)
#     Sulfate = models.FloatField(default=0.0)
#     Conductivity = models.FloatField(default=0.0)
#     Organic_carbon = models.FloatField(default=0.0)
#     Trihalomethanes = models.FloatField(default=0.0)
#     Turbidity = models.FloatField(default=0.0)

# class Results(models.Model):
#     Potability = models.IntegerField(0)

