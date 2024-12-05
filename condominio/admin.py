from django.contrib import admin

from condominio.models import CondominioModel, CasaModel

# Register your models here.

admin.site.register(CasaModel)
admin.site.register(CondominioModel)