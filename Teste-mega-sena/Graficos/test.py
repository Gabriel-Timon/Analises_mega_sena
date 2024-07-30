import pandas as pd
import matplotlib.pyplot as plt
import analises
import seaborn as sns
from collections import Counter

# Carregar dados
file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)


# Gráfico de Linhas dos Ganhadores ao Longo do Tempo
df['Ano'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.year
ganhadores_6 = df.groupby('Ano')['6 acertos'].sum()
ganhadores_5 = df.groupby('Ano')['5 acertos'].sum()
ganhadores_4 = df.groupby('Ano')['4 acertos'].sum()
plt.figure(figsize=(14, 6))
plt.plot(ganhadores_6.index, ganhadores_6.values, marker='o', linestyle='-', label='6 acertos')
plt.plot(ganhadores_5.index, ganhadores_5.values, marker='o', linestyle='-', label='5 acertos')
plt.plot(ganhadores_4.index, ganhadores_4.values, marker='o', linestyle='-', label='4 acertos')
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Número de Ganhadores', fontsize=14)
plt.title('Número de Ganhadores por Ano', fontsize=16, pad=20)
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()



# Histograma do valor dos prêmios de 6 acertos
df['Rateio 6 acertos'] = df["Rateio 6 acertos"].apply(analises.converter_float)
plt.figure(figsize=(14, 6))
plt.hist(df['Rateio 6 acertos'], bins=20, color='blue', edgecolor='black')
plt.title('Distribuição do Valor dos Prêmios de 6 acertos', fontsize=16, pad=20)
plt.xlabel('Valor do Prêmio', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.grid(True)
plt.show()


# Boxplot do valor dos prêmios de 4, 5 e 6 acertos
df['Rateio 5 acertos'] = df["Rateio 5 acertos"].apply(analises.converter_float)
df['Rateio 4 acertos'] = df["Rateio 4 acertos"].apply(analises.converter_float)
data = [df['Rateio 4 acertos'], df['Rateio 5 acertos'], df['Rateio 6 acertos']]
plt.figure(figsize=(14, 6))
plt.boxplot(data, labels=['4 acertos', '5 acertos', '6 acertos'])
plt.title('Boxplot do Valor dos Prêmios', fontsize=16, pad=20)
plt.xlabel('Categoria de Acertos', fontsize=14)
plt.ylabel('Valor do Prêmio', fontsize=14)
plt.grid(True)
plt.show()


# Heatmap de correlação entre as bolas sorteadas
numeros_sorteados = df[["N1", "N2", "N3", "N4", "N5", "N6"]]
correlacao = numeros_sorteados.corr()
plt.figure(figsize=(14, 6))
sns.heatmap(correlacao, annot=True, cmap='coolwarm')
plt.title('Heatmap de Correlação entre as Bolas Sorteadas', fontsize=16, pad=20)
plt.show()


# Gráficos de dispersão entre as bolas sorteadas
plt.figure(figsize=(19, 13))
for i, (bola1, bola2) in enumerate([("N1", "N2"), ("N1", "N3"), ("N1", "N4"), ("N1", "N5"), ("N1", "N6"),
                                    ("N2", "N3"), ("N2", "N4"), ("N2", "N5"), ("N2", "N6"),
                                    ("N3", "N4"), ("N3", "N5"), ("N3", "N6"),
                                    ("N4", "N5"), ("N4", "N6"),
                                    ("N5", "N6")]):
    plt.subplot(4, 4, i + 1)
    plt.scatter(df[bola1], df[bola2], alpha=0.5, edgecolors='w', linewidth=0.5)
    plt.xlabel(bola1)
    plt.ylabel(bola2)
    plt.title(f'Dispersão: {bola1} vs {bola2}')
plt.tight_layout()
plt.suptitle('Gráficos de Dispersão entre as Bolas Sorteadas', y=1.02, fontsize=16)
plt.show()