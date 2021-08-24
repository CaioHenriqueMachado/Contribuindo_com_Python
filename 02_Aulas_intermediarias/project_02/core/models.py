from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo      = models.CharField(max_length=100)
    descricao   = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    created_at  = models.DateTimeField(auto_now=True)

    # dessa forma a tabela irá se chamar core_evento, para forçar um nome tem a classe abaixo:
    class Meta:
        db_table = 'evento'