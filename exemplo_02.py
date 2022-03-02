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

data = pd.read_csv('datasets/kc_house_data.csv')
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

cols = ['price','id','date']
print(data.loc[0:10,cols])