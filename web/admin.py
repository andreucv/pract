from django.contrib import admin
from web.models import *

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Comentario)
admin.site.register(Prioridad)
admin.site.register(Estado)
admin.site.register(Idioma, IdiomaAdmin)