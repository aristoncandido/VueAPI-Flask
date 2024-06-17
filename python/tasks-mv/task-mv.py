import pandas as pd #importando pandas
import json
#dataFrame = pd.DataFrame()




alunos_df = pd.read_excel('./dados/Analise de Matriculas WR Educacional.xlsx')



#print(alunos_df.head()) #5 primeiras linhas, OU quantas quiser
## print(alunos_df.shape) #mostra apenas linhas e colunas
#print(alunos_df.describe()) ##medias e informações bases da planilhas
#pegar intervalo de lihas especifico 
#print(alunos_df.loc[1:5])#pega da linha 1 ate a 5

alunos_df = alunos_df.dropna(axis=1, how='all') #tirando todos os valores NaN em colunas
alunos_df = alunos_df.rename(columns={"Esporte":"area"}) #mudei o nome da coluna Esporte para Área
alunos_df = alunos_df.rename(columns={"data_nascimento":"data"}) #mudei o nome da coluna data_nasc 
alunos_df = alunos_df.rename(columns={"ID da Turma":"id"})
alunos_df = alunos_df.rename(columns={"Turno":"turno"})
alunos  = alunos_df.to_json('alunos.json',orient='records',force_ascii=False,indent=4, date_format='iso') ## convertendo cada registro em ojeto, 
                                                                                                          ## ajustando o formato ascii para aceitar acento
                                                                                                          ## Ajustando indentacao para 4 e formatando a data para ISO   



