#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 00:33:42 2021

@author: caio
"""

from datetime import date, time, datetime, timedelta


# Class date: 

# Assumindo data 30/08/2021 para o teste funcionar
data_atual = date(year= 2021, month= 8, day= 30)

# Para puxar a data atual
#data_atual = date.today()

result = str(type(data_atual))
assert( result == "<class 'datetime.date'>" )

result = str(data_atual)
assert( result == "2021-08-30" )

result = data_atual.strftime('%d-%m-%Y')
assert( result == "30-08-2021" )

result = data_atual.strftime('%d/%m/%Y')
assert( result == "30/08/2021" )

result = data_atual.strftime('%d %m %Y')
assert( result == "30 08 2021" )

result = data_atual.strftime('%d %m %y')
assert( result == "30 08 21" )

result = data_atual.strftime('%A %B %Y')
assert( result == "Monday August 2021" )


# Class time:

# Assumindo horário 10:50:35 para o teste funcionar
hora_atual = time(hour=10, minute=50, second=35)

# Não parece puxar a hora atual, se não achar pega a hora do datetime (linha 78)
#hora_atual = time()

result = str(type(hora_atual))
assert( result == "<class 'datetime.time'>" )

result = str(hora_atual)
assert( result == "10:50:35" )

result = hora_atual.strftime('%H-%M-%S')
assert( result == "10-50-35" )

result = hora_atual.strftime('%H:%M:%S')
assert( result == "10:50:35" )

result = hora_atual.strftime('%H %M %S')
assert( result == "10 50 35" )


# Class datetime:

# Assumindo data 30/08/2021 e hora 10:50:35 para o teste funcionar
data_hora_atual = datetime(year= 2021, month= 8, day= 30, hour=10, minute=50, second=35)

# Para puxar a data e hora atual
#data_hora_atual = datetime.now()

result = str(type(data_hora_atual))
assert( result == "<class 'datetime.datetime'>" )

result = str(data_hora_atual)
assert( result == "2021-08-30 10:50:35" )

result = data_hora_atual.strftime('%H:%M:%S %d/%m/%Y')
assert( result == "10:50:35 30/08/2021" )

result = data_hora_atual.strftime('%d/%m/%Y')
assert( result == "30/08/2021" )

result = data_hora_atual.strftime('%H:%M:%S')
assert( result == "10:50:35" )

result = data_hora_atual.strftime('%c')
assert( result == "Mon Aug 30 10:50:35 2021" )

result = str(data_hora_atual.date())
assert( result == "2021-08-30" )

result = str(data_hora_atual.time())
assert( result == "10:50:35" )

result = str(data_hora_atual.second)
assert( result == "35" )

result = str(data_hora_atual.minute)
assert( result == "50" )

result = str(data_hora_atual.hour)
assert( result == "10" )

result = str(data_hora_atual.weekday())
assert( result == "0" )
tupla = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom')
assert( tupla[int(result)] == "Seg" )

result = str(data_hora_atual.month)
assert( result == "8" )

result = str(data_hora_atual.year)
assert( result == "2021" )

# Criando data 
result = str(datetime(2020, 9, 10, 15,30,59))
assert( result == "2020-09-10 15:30:59" )

# convertendo string para type data
data = '10/01/2029 12:06:20'
result = str(type(datetime.strptime(data,'%d/%m/%Y %H:%M:%S')))
assert( result == "<class 'datetime.datetime'>" )

# Adicionando 1 ano
data = '10/01/2029 12:06:20'
result = datetime.strptime(data,'%d/%m/%Y %H:%M:%S') + timedelta(days=365)
assert( str(result) == "2030-01-10 12:06:20" )

# Removendo 6 minutos e 20 segundos
data = '10/01/2029 12:06:20'
result = datetime.strptime(data,'%d/%m/%Y %H:%M:%S') - timedelta(minutes=6, seconds=20)
assert( str(result) == "2029-01-10 12:00:00" )



















