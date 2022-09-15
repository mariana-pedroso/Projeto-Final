"""
Projeto Final_Mariana Foletto Pedroso
Requisito: Aplica��o que grava balancete, cria arquivo, l� e grava o conte�do em novo arquivo.
Autor: Mariana Foletto Pedroso
Vers�o: 0.0.1
Data: 15/09/2022.
"""


# Importa��o pacotes

import requests as rq
import pandas as pd
import openpyxl as xl

# Gravando em disco o conte�do da vari�vel dados em arquivo chamamdo balancete.csv

URL = 'https://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
dados = rq.get(URL)
dados.save('balancete.csv')


# Lendo o arquivo balancete.csv para a vari�vel balancete


balancete = pd.read_csv('balancete.csv', sep = ',')


# Gravando em disco conte�do de balancete em arquivo balencete.xlsx

balancete.save('balancete.xlsx')


# Lendo o arquivo balancete.xlsx para a vari�vel novo_balancete

novo_balancete = xl.read_xlsx('balancete.xlsx', sep = ',')


# Gravando conte�do da vari�vel novo balancete no arquivo novo balancete.xlsx

novo_balancete.save('novo_balancete.xlsx')


    