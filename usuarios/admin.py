from django.contrib import admin
from .models import Casa

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
