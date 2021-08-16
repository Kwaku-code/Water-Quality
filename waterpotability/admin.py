from django.contrib import admin
from .models import Variables
# Register your models here.


[admin.site.register(X) for X in [Variables]]
