# script aula02 do Curso Python do Zero ao DS do Meigarom (Seja um Datascientist).
#
# importar/declarar a library Pandas e carregar o DataFrame para memória
#
import pandas as pd

#data = pd.read_csv('datasets/kc_house_data.csv')

# função que converte de object (string) -> date
#data['date'] = pd.to_datetime(data['date'])

# mostrar na tela os tipos de variáveis de cada coluna
#print(data.dtypes)

# ===================================
# Como converter os tipos de variáveis
# ===================================
#
# Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)

# Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)

# Float -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(Int64)

# Inteiro -> String
#data['bedrooms'] = data['bedrooms'].astype(str)

#print(data.dtypes)

# Inteiro -> Float
#data['bedrooms'] = data['bedrooms'].astype(float)

# String -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(Int64)

# String -> Data
#data['date'] = pd.to_datetime(data['date'])

# ===================================
# Criando novas variáveis
# ===================================

#data = pd.read_csv('datasets/kc_house_data.csv')

#data['nome_do_meigarom'] = "meigarom" 

#data['comunidade_ds'] = 80
#data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-28')

#print(data.columns)

#print(data[['id','date','nome_do_meigarom','comunidade_ds','data_abertura_comunidade_ds']].head())

##print(data.dtypes)

# ===================================
# Deletando variáveis
# ===================================

#print(data.columns)
#data = data.drop('nome_do_meigarom')
#cols = ['nome_do_meigarom','comunidade_ds','data_abertura_comunidade_ds']
#data = data.drop(cols, axis=1)
#print(data.columns)

# ===================================
# Selecionar dados, forma 01: Direto pelo nome das colunas
# ===================================

#data = pd.read_csv('datasets/kc_house_data.csv')
#print(data[['price','id','date']])

# ===================================
# Selecionar dados, forma 02: Pelos índices das linhas e colunas
# ===================================
# DADOS [LINHAS, COLUNAS]

#print(data.iloc[0:10,0:3])

#todas colunas, por exemplo

#print(data.iloc[0:10,:])

# ===================================
# Selecionar dados, forma 03: Pelos índices das linhas e nome das colunas
# ===================================

#cols = ['price','id','date']
#print(data.loc[0:10,cols])

# ===================================
# Selecionar dados, forma 04: Pelos índices booleanos
# ===================================

# 1, 0
# True, False

#cols = [True, False, True, True, False, False,False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

#print(data.loc[0:10,cols])

#print(data.columns)

# ===================================
# Respondendo as perguntas de negócio
# ===================================

data = pd.read_csv('datasets/kc_house_data.csv')

# 1. Qual a data do imóvel mais antigo do portfólio?

#data['date'] = pd.to_datetime(data['date'])
#print(data.sort_values('date', ascending=True))

# 2. Quantos imóveis possuem o numero máximo de andares?

#print(data['floors'].unique()
#print(data[data['floors'] == 3.5].shape)

# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
# 	Acima de 540.000 -> Alto Padrão
# 	Abaixo de 540.000 -> Baixo Padrão

#data['level'] = 'standard'

#data.loc[data['price'] > 540000, 'level'] = 'high_level'
#data.loc[data['price'] < 540000, 'level'] = 'low_level'

# 4. Gostaria de um relatório ordenado pelo preço e contendo as seguintes informações:
#    ( id do imóvel, data em que ficou disponível para compra, o numero de quartos, o tamanho total do terreno, o preço e a classificação do imóvel ( alto e baixo padrão ) ).


#report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price', ascending=False)

#print(data.columns)

#print(report.head())

 #Não se pode esquecer de usar o parâmetro ", index=False", pois se não ele vai exportar com os index's originais e na hora de fazer a leitura desse CSV os dados ficarão totalmente embaralhados

#report.to_csv('datasets/report_aula02.csv', index=False)

# 5. Gostaria de um mapa indicando onde as casas estão localizadas geograficamente.
# Plotly - Biblioteca que armazena uma funcao que desenha mapa
#Para instalar, via terminal: pip install plotly
# Scatter MapBox - Funcao que desenha mapa

#import plotly.express as px

#data_mapa = data[['id', 'lat', 'long', 'price']]

#mapa = px.scatter_mapbox (data_mapa, lat= 'lat', lon = 'long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

#mapa.update_layout( mapbox_style='open-street-map')
#mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
#mapa.show()

#mapa.write_html('datasets/mapa_house_rocket.html')
#testar arquivo gerado em HTML com mais calma, pois o atual não está abrindo nos navegadores Android.

# linha apenas para testar DF
#print(data.head())

# ===================================
# Exercícios Práticos abaixo
# ===================================

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#	1. Crie uma nova coluna chamada: "house_age".
#		- Se o valor da coluna date for maior que 2014-01-01 => "new_house"
#		- Se o valor da coluna date for menor que 2014-01-01 => "old_house"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#print(data.dtypes)

#print(data['date'].head())

import numpy as np

data['date'] = pd.to_datetime(data['date'])

#data['date'] = pd.to_datetime(data['date'])
#print(data.sort_values('date', ascending=True))

#print(data['date'].head())

#conditions = [
#    (df['Set'] == 'Z') & (df['Type'] == 'A'),
#    (df['Set'] == 'Z') & (df['Type'] == 'B'),
#    (df['Type'] == 'B')]
#choices = ['yellow', 'blue', 'purple']
#df['color'] = np.select(conditions, choices, default='black')
#print(df)
###
#CondsQ1 = [ (data['date'] > '2014-01-01'), (data['date'] < '2014-01-01') ]

#SelsQ1 = ['new_house', 'old_house']

#data['house_age'] = np.select(CondsQ1,SelsQ1)

#print(data.head())
###
#print(data[data['house_age'] == 'new_house'].shape)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 1 finalizado
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#2. Crie uma nova coluna chamada: "dormitory_type"
#		- Se o valor da coluna "bedrooms" for igual a 1 => "studio"
#		- Se o valor da coluna "bedrooms" for igual a 2 => "apartament"
#		- Se o valor da coluna "bedrooms" for maior que 2 => "house"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

CondsQ2 = [(data['bedrooms'] == 1), (data['bedrooms'] == 2), (data['bedrooms'] > 2)]

SelsQ2 = ['studio', 'apartment', 'house']

data['dormitory_type'] = np.select (CondsQ2, SelsQ2)

print(data.head())

print(data[data['dormitory_type'] == 'house'].shape)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 2 finalizado
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
	#Acima de 540.000 -> Alto Padrão
#	Abaixo de 540.000 -> Baixo Padrão
#	
#	- Criar uma nova coluna no conjunto de dados chamada "standard"
#		- Para cada linha, eu vou comparar com a coluna "price"
#			- Se "price" for maior que 540.000, eu vou escrever "high_standard" na coluna "standard"
#			- Se "price" for menor que 540.000, eu vou escrever "low_standard" na coluna "standard"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

<<<<<<< HEAD
#print(data.dtypes)
#print(data['price'].head())

CondsQ3 = [(data['price'] > 540000), (data['price'] < 540000)]

SelsQ3 = ['high_standard', 'low_standard']

data['standard'] = np.select(CondsQ3, SelsQ3)

#print(data.head())

#print('\n\n\nLow Standard: ',data[data['standard'] == 'low_standard'].shape)

#print(data[['id','price','standard']].head())

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Exercício 3 repetido finalizado, logo abaixo o exercício 3 correto.
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#3. Crie uma nova coluna chamada: "condition_type"
#		- Se o valor da coluna "condition" for menor ou igual a 2 => "bad"
#		- Se o valor da coluna "condition" for igual a 3 ou 4 => "regular"
#		- Se o valor da coluna "condition" for igual a 5 => "good"

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#





data['condition_type'] = 'condition'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'

#cols = ['price','id','date']
#print(data.loc[0:10,cols])

#data['level'] = 'standard'

#data.loc[data['price'] > 540000, 'level'] = 'high_level'

#
#print(data.columns)

#id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#       'lat', 'long', 'sqft_living15', 'sqft_lot15', 'standard'

=======
>>>>>>> parent of 76f1d75 (Finalizando Q4.)
