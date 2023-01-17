from django.contrib import admin
from allenamento.models import Tipi, Esercizio,Schedario,Blocco,Muscoli

# Register your models here.

admin.site.register(Tipi)
admin.site.register(Muscoli)
admin.site.register(Schedario)
admin.site.register(Blocco)
admin.site.register(Esercizio)


