# script aula02 do Curso Python do Zero ao DS do Meigarom (Seja um Datascientist).
#
# importar/declarar a library Pandas e carregar o DataFrame para memória
#
import pandas as pd

data = pd.read_csv('datasets/kc_house_data
csv')

# função que converte de object (string) -> date
data['date'] = pd.to_datetime(data['date'])

# mostrar na tela os tipos de variáveis de cada coluna
print(data.dtypes)

# ===================================
# Como converter os tipos de variáveis
# ===================================
#
# Inteiro -> Float
data['bedrooms'] = data['bedrooms'].astype(float)

# Inteiro -> Float
data['bedrooms'] = data['bedrooms'].astype(float)

# Float -> Inteiro
data['bedrooms'] = data['bedrooms'].astype(Int64)

# Inteiro -> String
data['bedrooms'] = data['bedrooms'].astype(str)

#print(data.dtypes)

# Inteiro -> Float
data['bedrooms'] = data['bedrooms'].astype(float)

# String -> Inteiro
data['bedrooms'] = data['bedrooms'].astype(Int64)

# String -> Data
data['date'] = pd.to_datetime(data['date'])

# ===================================
# Criando novas variáveis
# ===================================

data['nome_do_meigarom'] = "meigarom"
