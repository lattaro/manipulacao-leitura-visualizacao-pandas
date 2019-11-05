import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\Python\\Ciência_Dados\\Dados_2.csv') #o endereço precisa ter duas barras para funcionar
print(df.head()) #por padrão o .head traz as 5 primeiras linhas
print (df.head(n=10)) #é possível especificar a qnt de linhas a serem impressas
print(df.tail()) #.tail imprime as últimas linhas

print (df["bairro"].value_counts()) #soma o total de valores baseados no index referenciado
print (df["bairro"].unique()) #traz os "bairros" existentes em formato de vetor
print (df["bairro"].value_counts(normalize=True)) # normaliza a referência retornando uma porcentagem
print(df.groupby("bairro").mean()) #agrupa por bairro (referencia) e calcula a médias das colunas
print(df.groupby("bairro").mean()["pm2"].sort_values()) #agrupa por bairro e calcula a média. ordena por pm2
def truncar (bairro): #função para exibir apenas as 3 primeiras letras dos nomes dos bairros
    return bairro[:3]
print(df["bairro"].apply(truncar)) #.apply aplica a função criada aos dados.
print(df["bairro"].apply(lambda x: x[:3])) #modo mais sucinto de aplicar a função anterior usando a lambda
df2 = df.head() #cria um novo dataframe com as 5 primeiras linhas do df original
df2 = df2.replace({"pm2":{12031.25: np.nan}}) #substitui um valor específico por um NaN
print (df2)
print (df2.dropna()) #o pandas retira as linhas que contém um NaN e mantém a indexação.
print (df2.fillna(99)) #preenche as linhas contendo NaN por um número específico sem alterar o df2 original
print(df2.isna()) #retorna quem é q e quem não é NaN
df["preco"].plot.hist() #gráfico (histograma) da distribução dos preços em uma escala *10^7. Os dados são divididos em 10 partes
#plt.show() #imprime o gráfico
df["preco"].plot.hist(bins=30, edgecolor='black') # aqui especificamos que queremos divirid os dados em 30 partes
                                                # também foi especificado a cor da borda do gráfico
#plt.show()
#df["bairro"].value_counts().plot.bar() #gráfico de barras agrupado por bairro, exibido verticalmente
#plt.show()
#df["bairro"].value_counts().plot.barh()
#plt.show()
#df["bairro"].value_counts().plot.barh(title="Número de apartametos") #é posível dar um nome para o gráfico
#plt.show()
#df.plot.scatter(x='preco', y='area') #gráfico de disperção no qual x recebe preço e y recebe area
#plt.show()
#plt.style.use('ggplot') #define o estilo dos gráficos. será utilizado em todos os gráficos gerados após esta linha
#df.plot.scatter(x='pm2', y='area')
#plt.show()
#print(plt.style.available) #mostra os estilos de gráficos disponíveis
#df["quartos"].value_counts().plot.pie() #gráfico em forma de pizza, agrupado por qnt de quartos.
#plt.show()

df3 = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"], #cria um novo dataframe
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})
df3.to_csv("aulas.csv") #.to_csv salva este dataframe em um formato csv
print(pd.read_csv("aulas.csv"))
