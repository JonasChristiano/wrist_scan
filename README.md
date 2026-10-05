# Wrist Scan

Protótipo educacional de descoberta de hosts e consulta de portas TCP, com interface web em Flask.

## Funcionalidades implementadas

- Entrada de endereço IP pela interface.
- Descoberta de hosts por chamadas ao comando `ping`.
- Consulta de portas TCP e tentativa de leitura de banners.
- Exibição dos resultados em páginas HTML.

## Tecnologias

Python, Flask, sockets, threads, HTML e CSS. O código usa `match`, portanto requer Python 3.10 ou superior.

## Executar em ambiente local

```bash
git clone https://github.com/JonasChristiano/wrist_scan.git
cd wrist_scan
python -m venv .venv
```

Ative o ambiente virtual conforme seu sistema e execute:

```bash
python -m pip install Flask colorama
python app.py
```

Abra `http://127.0.0.1:5000`. Execute consultas apenas em um laboratório ou uma rede sob sua administração.

## Estado e limitações

Projeto de estudo, sem validação para uso em produção. A descoberta usa opções de `ping` do Windows (`-n` e `-w`) e depende da presença de `TTL` na resposta; não funciona da mesma forma no Linux.

A varredura de todas as portas cria muitas threads e pode consumir recursos elevados. Priorize portas específicas. O servidor utiliza o modo de desenvolvimento do Flask. A validação de entradas e o tratamento de erros ainda precisam de refinamento.

[Autor: Jonas Christiano](https://github.com/JonasChristiano)
