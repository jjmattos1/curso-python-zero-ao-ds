#Grupo de estudos no Telegram, mensagem da data 15/01/21.
#BOM DIA GALERAAAA, TUDO BEM COM VOCÊS!! 
#Para fechar a AULA 01 de PYTHON do ZERO ao DS:

#Essas são as respostas finais com os códigos:

#1. Quantas casas estão disponíveis para compra?
# R: 21613
#print( df1.shape[0] )

#2. Quantos atributos as casas possuem?
# R: 21
#print( df1.shape[1] )

#3. Quais são os atributos das casas?
#print( df1.columns )

#4. Qual a casa mais cara ( casa com o maior valor de venda )?
# R: O imóvel com o id 6762700020 é o mais caro
#print( df1[['id', 'price']].sort_values( 'price', ascending=False ) )

#5. Qual a casa com o maior número de quartos?
# R: O imóvel com o id 2402100895 tem 33 quartos
#print( df1[['id', 'bedrooms']].sort_values( 'bedrooms', ascending=False ) )

#6. Qual a soma total de quartos do conjunto de dados?
# R: A soma total de quartos é de 72854
#print( df1['bedrooms'].sum() )

#7. Quantas casas possuem 2 banheiros?
# R: 1930 imóveis possem 2 banheiros
#print( df1[df1['bathrooms'] == 2].shape )

#8. Qual o preço médio de todas as casas no conjunto de dados?
# R: O preço médio dos imóvesi do conjunto de dados é de R$ 540.088,14
#print( df1['price'].mean() )

#9. Qual o preço médio de casas com 2 banheiros?
# R: O preço médio das casas com 2 banheiros é de R$ 457.889,71
#print( df1.loc[df1['bathrooms'] == 2, 'price'].mean() )
#    
#10. Qual o preço mínimo entre as casas com 3 quartos?
# R: O preço mínimo das casas de 3 quartos é de R$ 82.000,0
#print( df1.loc[df1['bedrooms'] == 3, 'price'].min() )

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
# OBS: 1 pé quadrado = 0,09 metros quadrados
# R: 2141 imóveis possuem mais de 300 metros quadrados na sala de estar.
#df1['m2_living'] = df1['sqft_living'] * 0.092
#print( df1[df1['m2_living'] > 300].shape )

#12. Quantas casas tem mais de 2 andares?
# R: 782 imóveis tem mais de 2 andares
#print( df1[df1['floors'] > 2].shape )

#13. Quantas casas tem vista para o mar?
# R: 163 imóves tem vista para o mar
#print( df1[df1['waterfront'] == 1].shape )

#14. Das casas com vista para o mar, quantas tem 3 quartos?
# R: 64 imóveis tem vista para o mar e possuem 3 quartos
#print( df1[(df1['waterfront'] == 1 ) & ( df1['bedrooms'] == 3 )].shape )

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
# R: 288 imóveis tem mais de 300 metros quadrados de sala de estar e mais de 2 banheiros
#print( df1[(df1['m2_living'] > 300) & (df1['bathrooms'] > 2)].shape )

#Espero que vocês tem se DIVERTIDO E APRENDIDO MUITO.

#Estou muito feliz em ver todo o empenho de vocês! De verdade.

#Tiveram pessoas que chegaram aqui sem saber nem o que é Python e já estão resolvendo questões de negócio!!
#PARABENS PELO ESFORÇO e CONTINUEM ASSIM!!

#VAMOS EM FRENTE!