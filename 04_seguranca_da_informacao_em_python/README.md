<h1 align="center" id="1">My notes about Python - Conceitos de Segurança</h1>

> *Para entender os conceitos intermediários foi desenvolvido um projeto para aplicar todos os conceitos abordados. Nesse README estão apenas as informações iniciais para fazer um projeto usando Flask.

<img src="../img/line.png" alt="line" width="100%">
<br>

## SUMÁRIO
 - [Introdução](#0_0)
 - [Ping](#0_1)
 - [Biblioteca Socket, TCP, UDP](#0_2)
 - [Ferramentas](#0_3)
 - [Instalando Pacotes](#0_4)
 - [requirements](#0_5)
 - [Recursos da API](#0_6)

<img src="../img/line.png" alt="line" width="100%">
<br>

<h3 id="0_0">Introdução</h3>

**Segurança da informação**
<p align="justify"> Essa área tem como objetivo assegurar que todos os dados de uma ou mais informações estejam sempre <b>confidenciais, íntegros e disponíveis</b> em qualquer meio de comunicação.</p>

**Principios da segurança da informação:**

- Integridade
- Confidencialidade
- Disponibilidade
- Identificação
- Autenticação
- Autorização
- Não Repúdio

<br>

<h3 id="0_1">Ping</h3>

**ICMP:** Protocolo pertencente ao protocolo IP, utilizados para fornecer relatórios de erros.

Ping: ferramenta que utiliza o protocolo ICMS, para testar a conectividade entre nós.

Envia uma requisição, e recebe uma resposta informando se o destino está ativo ou não.

<br>

**Alguns parâmetros do comando ping**

**(-t):** Utilizando o -t, o comando ficará enviando pacotes até o usuário forçar a parada (com Ctrl + C).

**(-a) no Windows / (host) no Linux/Mac:** No Windows: Além de testar a conectividade, também tentará resolver o hostname da máquina pingada.

**(-n) no Windows / (-c) no Linux:** O comando define o número de pacotes a ser enviado.
Sintaxe: -c 8 site.com.br (8 pacotes serão enviados pelo comando).


> Exemplo: [Ping Simples](./01_ping.py)
> Exemplo: [Ping Múltiplo](./02_ping_multiplo.py)

<br>

<h3 id="0_2">Biblioteca Socket</h3>

**Biblioteca Socket:** Esta biblioteca fornece acesso de baixo nível à interface de rede.


**TCP** - (Transmission Control Protocol) ou Protocolo de Controle de Transmissão. Verifica se os dados são enviados na sequência correta e sem erros.

> Exemplo: [Cliente TCP](./03_cliente_tcp.py)

**UDP** - (User DatagramProtocol) ou Protocolo de Datagrama de usuário.

Aplicação do método three handshake

> Exemplo: [Cliente UDP](./04_pt1_cliente_udp.py)
> Exemplo: [Servidor UDP](./04_pt2_servidor_udp.py)


<h3 id="0_3">Ferramentas</h3>

**Biblioteca random**

Gera números letras, simbolos e letras aleatórios.

<br>

**Hash**

É como se fosse um identificador único.

Site que gera hash e também descripta hash: https://md5decrypt.net/en/

> Em Python existe a Biblioteca haslib que implementa hashs seguras como SHA1, SHA256, MD5

<br>

**Multithreading**

Threading é o processo, no ambiente Multithreading, cada processo pode responder diversar solicitações concorrente ou simultaneamente.

> Em Python existe a Biblioteca threading

**Biblioteca ipaddress**

Biblioteca capaz de criar, manupular endereços IP do tipo IPv4, IPv6 e até redes inteiras.


<h3 id="0_4">Gerador de senhas</h3>


> Exemplo: [Gerado de senhas](./05_gerador_senha.py)

<br>

<h3 id="0_5">Comparador de Hashs</h3>


> Exemplo: [Comparador de Hashs](./06_comparador_hashs.py)

<br>

<h3 id="0_6">Threads</h3>


> Exemplo: [Threads](./07_thread.py)

<br>

<h3 id="0_7">IPs</h3>


> Exemplo: [IPs](./08_ip.py)

<br>

<h3 id="0_8">Gerador de Hashs</h3>


> Exemplo: [Comparador de Hashs](./09_gerador_hashs.py)

<br>

<h3 id="0_9">Gerador de Wordlist</h3>

Wordlist são arquivos contendo uma palavra por linha.

> Exemplo: [Comparador de Hashs](./10_gerador_wordlists.py)

<br>

<h3 id="0_10">Web scraping</h3>

Web scraping é uma ferramenta de coleta de dados web

> Exemplo: [Comparador de Hashs](./11_web_scraping.py)

<br>

<h3 id="0_11">Web Crawler</h3>

Web Crawler é uma ferramenta para encontrar, ler e indexar paginas de um site.
Usado para levantamento de informações

> Exemplo: [Comparador de Hashs](./12_web_crawler.py)

<br>

<h3 id="0_11">Verificador de Telefone</h3>

Web Crawler é uma ferramenta para encontrar, ler e indexar paginas de um site.
Usado para levantamento de informações

> Exemplo: [Comparador de Hashs](./12_web_crawler.py)

<br>

<h3 id="0_11">Ocultador de arquivos</h3>

Web Crawler é uma ferramenta para encontrar, ler e indexar paginas de um site.
Usado para levantamento de informações

> Exemplo: [Comparador de Hashs](./12_web_crawler.py)

<br>

<h3 id="0_11">Verificador de IP externo</h3>

Web Crawler é uma ferramenta para encontrar, ler e indexar paginas de um site.
Usado para levantamento de informações

> Exemplo: [Comparador de Hashs](./12_web_crawler.py)

<br>


<h3 id="0_11">Ferramenta grafica para abrir o navegador</h3>

Web Crawler é uma ferramenta para encontrar, ler e indexar paginas de um site.
Usado para levantamento de informações

> Exemplo: [Comparador de Hashs](./12_web_crawler.py)

<br>



 - [Voltar ao topo](#1)
 - [Voltar ao menu principal](https://github.com/CaioHenriqueMachado/Contribuindo_com_Python/#1)

<br>
<img src="../img/line.png" alt="line" width="100%">