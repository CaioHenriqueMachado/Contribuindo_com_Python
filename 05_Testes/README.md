<h1 align="center" id="1">My notes about Python - Testes em Python</h1>

> *Para entender os conceitos intermediários foi desenvolvido um projeto para aplicar todos os conceitos abordados. Nesse README estão apenas as informações iniciais para fazer um projeto usando Flask.

<img src="../img/line.png" alt="line" width="100%">
<br>

## SUMÁRIO
 - [Introdução](#0_0)
 - [TDD](#0_1)
 - [Testes unitários](#0_2)


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

<h3 id="0_1">TDD</h3>

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

<h3 id="0_2">Testes unitários</h3>

Esta biblioteca fornece acesso de baixo nível à interface de rede.


**TCP** - (Transmission Control Protocol) ou Protocolo de Controle de Transmissão. Verifica se os dados são enviados na sequência correta e sem erros.

> Exemplo: [Cliente TCP](./03_cliente_tcp.py)

**UDP** - (User DatagramProtocol) ou Protocolo de Datagrama de usuário.

Aplicação do método three handshake

> Exemplo: [Cliente UDP](./04_pt1_cliente_udp.py)
> Exemplo: [Servidor UDP](./04_pt2_servidor_udp.py)

<br>
 - [Voltar ao topo](#1)
 - [Voltar ao menu principal](https://github.com/CaioHenriqueMachado/Contribuindo_com_Python/#1)

<br>
<img src="../img/line.png" alt="line" width="100%">