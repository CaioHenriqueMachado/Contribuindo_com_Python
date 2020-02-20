#CODIGO liso e para clientes fieis.
import urllib.request
pagina= urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')   # mudou o codigo pois o preço nao esta no mesmo lugar.

texto= pagina.read().decode('utf8')
onde=texto.find('>$')
inicio=onde +2       # +2 pois voce nao que o >$ na respostar
fim= inicio +4        #+4 para pegar os 4 proximos
preço=texto[inicio:fim]
print(preço)
