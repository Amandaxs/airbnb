# airbnb
Repositório criado para armazenar os códigos referentes a análise dos dados da plataforma aberta airbnb

## 🚀 Começando

Após clonar o reposítório recomedo a criação de um virtual environment para instalr os pacotes necessários.  O virtual environment pode ser criado a partir do comando no terminal:

```
python -m venv .venv
```
após criação, é preciso mudar de diretório e ativar o environment no terminal

```
cd .venv
.venv\Scripts\activate
```

Após criação e ativação do environment, basta instalar os pacotes disponíveis no arquivo 'requiremente.txt' através do comando.
```
 pip install -r requirements.txt
```

Após os passos citados, o ambiente está pronto para rodar os notebooks no IDLE de sua preferência.

## 🚀 Arquivos

As análises são feitas através da metódologia crisp DM, que trabalha com etapas de entendimento de negócio, entendimento de dados, preparação de dados, modelagem e deployment.

A etapaa de entendimento de negócio foi feita através da leitura do documento disponibilizado e pesquisas na internet.

A etapa de entendimento e praparação dos dados foi feita no notebok chamado data_understanding_and_preparation.ipynb.

A Etapa de modelagem foi feita no notebook modeling.ipynb

Além disso existe um arquivo chamado utils.py que contém funções para auxiliar tanto no processo de preparação quanto de ajuste do modelo.

## 🚀 Dados

Os dados utilizados são o arquivo disponibilizado para este teste e arquivos de geolocalização da região da california  que beixei e disponibilizei na pasta data.

**É importante frisar que neste projeto deixarei a pasta de dados visivel por se tratarem de dados publicos, no entanto uma boa prática é manter a pasta de dados oculta através do arquivo gitignore**

## 🚀 Arquivos gerados

Durante a análise foi desenvolvido um relatóriogerado pelo pandas profilling que está salvo como html, o arquivo 'airbnb_data_report.html.

## 🚀 Convenções e padronizações

nome das variáveis e dados salvos estão no formato camel case

## Técnologias utilizadas:

[python](https://www.python.org/)

## Autora

Amanda Xavier