"""
Projeto Final_Mariana Foletto Pedroso
Requisito: Aplicação que grava balancete, cria arquivo, lê e grava o conteúdo em novo arquivo.
Autor: Mariana Foletto Pedroso
Versão: 0.0.1
Data: 15/09/2022.
"""


# Importação pacotes

import requests as rq
import pandas as pd
import openpyxl as xl

# Gravando em disco o conteúdo da variável dados em arquivo chamamdo balancete.csv

URL = 'https://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
dados = rq.get(URL)
dados.save('balancete.csv')


# Lendo o arquivo balancete.csv para a variável balancete


balancete = pd.read_csv('balancete.csv', sep = ',')


# Gravando em disco conteúdo de balancete em arquivo balencete.xlsx

balancete.save('balancete.xlsx')


# Lendo o arquivo balancete.xlsx para a variável novo_balancete

novo_balancete = xl.read_xlsx('balancete.xlsx', sep = ',')


# Gravando conteúdo da variável novo balancete no arquivo novo balancete.xlsx

novo_balancete.save('novo_balancete.xlsx')


    