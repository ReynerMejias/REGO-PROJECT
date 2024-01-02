from django.contrib import admin

# Register your models here.

from .models import Retiro, Peon, Contrato

admin.site.register(Retiro)
admin.site.register(Peon)
admin.site.register(Contrato)