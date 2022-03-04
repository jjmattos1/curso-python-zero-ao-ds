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
#print(report.head())

# Não se pode esquecer de usar o parâmetro ", index=False", pois se não ele vai exportar com os index's originais e na hora de fazer a leitura desse CSV os dados ficarão totalmente embaralhados
#report.to_csv('datasets/report_aula02.csv', index=False)

# 5. Gostaria de um mapa indicando onde as casas estão localizadas geograficamente.
# Plotly - Biblioteca que armazena uma funcao que desenha mapa
#Para instalar, via terminal: pip install plotly
# Scatter MapBox - Funcao que desenha mapa

import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox (data_mapa, lat= 'lat', lon = 'long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

mapa.update_layout( mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()

#mapa.write_html('datasets/mapa_house_rocket.html')
#testar arquivo gerado em HTML com mais calma, pois o atual não está abrindo nos navegadores Android.

# linha apenas para testar DF
#print(data.head())