from django.contrib import admin
from .models import Contacto


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'uuid')

admin.site.register(Contacto, ContactoAdmin)
