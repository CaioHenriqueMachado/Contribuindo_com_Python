from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
    titulo      = models.CharField(max_length=100)
    descricao   = models.TextField(blank = True, null =True)
    data_evento = models.DateTimeField(verbose_name = 'Data do Evento')
    created_at  = models.DateTimeField(auto_now =True, verbose_name= 'Data de criação')
    usuario     = models.ForeignKey(User, on_delete = models.CASCADE)


    # dessa forma a tabela irá se chamar core_evento, para forçar um nome tem a classe abaixo:
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y ás %H:%MHrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False