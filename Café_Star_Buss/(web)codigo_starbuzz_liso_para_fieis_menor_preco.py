#CODIGO liso e para clientes fieis.
#agora só mostra quando for menor que 4,74
import urllib.request
pagina= urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')   # mudou o codigo pois o preço nao esta no mesmo lugar.

texto= pagina.read().decode('utf8')
onde=texto.find('>$')
inicio=onde +2       # +2 pois voce nao que o >$ na respostar
fim= inicio +4        #+4 para pegar os 4 proximos
preço=float(texto[inicio:fim]) # ter que converter o texto para float.
if preço<4.74:
    print('Comprar!! Preço : %5.2f'%preço)
