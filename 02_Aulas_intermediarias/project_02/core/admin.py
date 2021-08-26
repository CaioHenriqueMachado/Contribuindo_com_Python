from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'created_at')
    list_filter = ('titulo', 'data_evento', ) #Não retire a vírgula do final

admin.site.register(Evento, EventoAdmin)