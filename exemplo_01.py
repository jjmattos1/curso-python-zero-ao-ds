# #mostre na tela a frase "Hello World"
# print("Hello World")
#
# #mostre na tela o resultado da soma de 30+50
# print(30+50)
# soma_de_numeros = 30 + 50
#
# #mostre o conteudo da variavel soma_de_numeros
# print(soma_de_numeros)

# carregue o conjunto de dados chamado kc_house_data.csv do HD para a memória

# funcao - read_csv()
# bilioteca - pandas

import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# mostre as 5 primeiras linhas do conjunto de dados

#print(data.head())

# mostre na tela o numero de colunas e o número de linhas do conjunto de dados

# print(data.shape)
#
# # mostre na tela o nome das colunas do conjunto de dados
# # CTRL+/ hotkey para comentar linhas selecionadas
#
# print(data.columns)
#
# # mostre na tela o conjunto de dados ordenados pela coluna price
#
# # print(data[['id','price']].sort_values('price'))
#
# # mostre na tela o conjunto de dados ordenados pela coluna price do maior pro menor
#
# print(data[['id','price']].sort_values('price',ascending=False))

# 5 - Qual a casa com o maior número de quartos?

#print(data[['id','bedrooms']].sort_values('bedrooms',ascending=False))

# mostrar qual e o tipo de dado de cada coluna
#print(data.dtypes)

# soma total de cada coluna usando a funcao sum do pandas, resposta pergunta 6
#print(data.sum())

# 7. Quantas casas possuem 2 banheiros?
#print(data[['id','bathrooms']].sort_values('bathrooms',ascending=False))
#print(data.bathrooms>=2)
# criar novo DF contendo apenas casas com mais de 2 banheiros. Ira gerar um DF boolean
#baths2 = data[baths2true]
#baths2true = data.bathrooms>=2

# como o resultado do filtro anterior é um DF boolean, entao se precisa criar um novo DF
# contendo apenas os resultados True, para so entao se poder manipular o mesmo
#baths2 = data[baths2true]

# agora se conta a QTD de linhas da dada coluna filtrada
#print(baths2['bathrooms'].count())

# Qual o preço medio de todas as casas do conjunto de dados?
#print(data['price'].mean())
#print(data.dtypes)

