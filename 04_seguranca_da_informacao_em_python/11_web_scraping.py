# Biblioteca de extração de dados de arquivos html e xml

from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content

# Recebendo todo o conteudo do site

soup = BeautifulSoup(site, 'html.parser')

# Trás todo o html da página
print(soup.prettify())

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
print(temperatura.string)

print(soup.title.string)
