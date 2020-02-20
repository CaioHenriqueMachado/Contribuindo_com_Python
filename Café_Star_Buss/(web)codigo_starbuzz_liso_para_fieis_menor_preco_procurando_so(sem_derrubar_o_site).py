#CODIGO liso e para clientes fieis.
#agora só mostra quando for menor que 4,74
import urllib.request
import time
preço=99.99

while preço >=4.74:
    pagina= urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')
    texto= pagina.read().decode('utf8')
    onde=texto.find('>$')
    inicio=onde +2      
    fim= inicio +4        
    preço=float(texto[inicio:fim])
    if preço>=4.74:
        time.sleep(600) #codigo para nao derrubar o site e dar espaço pra outros codigos
print('Comprar!! Preço : %5.2f'%preço)

#ataque DDoS  pois o programa nao espera para acessar o site de novo MAIS INFO: TWD388 python pra zumbi
