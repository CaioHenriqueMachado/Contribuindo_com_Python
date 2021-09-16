import re, json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
regiao = dados['region']

print('Detalhes IP EXTERNO\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}'.format(org, regiao, country, city, ip))


