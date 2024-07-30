# Gráficos dos dados registrados em analises.py

import pandas as pd
import analises
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter


# Carregar dados
file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)




'''

Gráfico de relação de ganhadores e não ganhadores de 6 acertos

'''
sorteios_1ganhador, mais_ganhadores, ninguem = analises.sorteios_ganhadores(df)
colors_1 = plt.cm.Blues(np.linspace(0.3, 0.8, 3))
plt.figure(figsize=(14, 6))
columns = plt.bar(['1 Ganhador', 'Mais de 1 Ganhador', 'Zero ganhadores'], 
        [sorteios_1ganhador, mais_ganhadores, ninguem], 
        color=colors_1)
for bar in columns:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0, height,
        f'{height:.0f}', ha='center', va='bottom', fontsize=12, color='black'
    )
plt.title('Quantidade ganhadores em relação a sorteios de 1 ganhador, mais de 1 ganhador e nenhum ganhador (6 acertos)', pad=20)
plt.ylabel('Quantidade de ganhadores', fontsize=14 ,labelpad=20)
plt.show()




'''

Gráfico do total de sorteios de 4, 5 e 6 acertos

'''
total_ganhadores_4_acertos, total_ganhadores_5_acertos, total_ganhadores_6_acertos = analises.total_ganhadores(df)
colors_3 = plt.cm.Reds(np.linspace(0.3, 1, 4))
plt.figure(figsize=(14, 6))
bars = plt.bar(['Total de sorteios com 6 acertos', 'Total de sorteios com 5 acertos', 'Total de sorteios com 4 acertos'],
        [total_ganhadores_4_acertos, total_ganhadores_5_acertos, total_ganhadores_6_acertos],
        color=colors_3)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0, height,
        f'{height:.0f}',  
        ha='center', va='bottom', fontsize=12, color='black'
    )
plt.title('Relação entre ganhadores de 4, 5 e 6 acertos', pad=20, fontsize=16)
plt.ylabel('Quantidade de ganhadores', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()





'''

Gráfico dos 10 números mais sorteados

'''
mais_sorteados = analises.numeros_mais_sorteados(df)
numeros = [num for num, _ in mais_sorteados]
frequencias = [freq for _, freq in mais_sorteados]
colors_2 = plt.cm.Greens(np.linspace(0.3, 1, 10))

def make_autopct(frequencias):
    def my_autopct(pct):
        total = sum(frequencias)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct

plt.figure(figsize=(15, 7))
plt.pie(frequencias, labels=numeros, colors=colors_2, autopct=make_autopct(frequencias), startangle=140)
plt.title('Os 10 números que mais foram sorteados', pad=20)
plt.axis('equal')
plt.legend(title='Números')
plt.show()



'''

Gráficos dos 5 estados mais sorteados

'''
# Dados
lst_estados_ganhadores = analises.estados_mais_ganhadores(df)
estados = [est for est, _ in lst_estados_ganhadores]
frequencia = [freq for _, freq in lst_estados_ganhadores]

# Subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 7))

# Gráfico de barras
colors = plt.cm.Purples(np.linspace(0.8, 0.2, len(estados)))
bars = ax[0].bar(estados, frequencia, color=colors)
for bar in bars:
    height = bar.get_height()
    ax[0].text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')
ax[0].set_xlabel('Estados', fontsize=14 , labelpad=20)
ax[0].set_ylabel('Frequência', fontsize=14 , labelpad=20)
ax[0].set_title('Os 5 estados mais sorteados (Quantitativo)', fontsize=16 , pad=20)



# Gráfico de pizza
colors_4 = plt.cm.Purples(np.linspace(0.3, 1, len(estados)))
ax[1].pie(frequencia, labels=estados, colors=colors_4, autopct='%1.1f%%', startangle=140)
ax[1].set_title('Os 5 estados mais sorteados (Porcentagem)', fontsize=16 , pad=20)
ax[1].axis('equal')
ax[1].legend()

# Para não sobrepor
plt.tight_layout()
plt.show()




'''

Gráfico de comparação de 4, 5 e 6 acertos durante os anos

'''
df['Ano'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.year

# Dados
ganhadores_4 = df.groupby('Ano')['4 acertos'].sum()
ganhadores_5 = df.groupby('Ano')['5 acertos'].sum()
ganhadores_6 = df.groupby('Ano')['6 acertos'].sum()

# Criar subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharex=True)

# Gráfico 4 acertos
axes[0].plot(ganhadores_4.index, ganhadores_4.values, marker='o', linestyle='-', label='4 acertos')
axes[0].set_xlabel('Ano', fontsize=14, labelpad=20)
axes[0].set_ylabel('Número de Ganhadores', fontsize=14, labelpad=20)
axes[0].set_title('Número de Ganhadores por Ano (4 acertos)', fontsize=16, pad=20)
axes[0].legend()
axes[0].grid(True)
formatter = FuncFormatter(lambda x, pos: '{:.0f}'.format(x))
axes[0].yaxis.set_major_formatter(formatter)

# Gráfico 5 acertos
axes[1].plot(ganhadores_5.index, ganhadores_5.values, marker='o', linestyle='-', label='5 acertos', color='green')
axes[1].set_xlabel('Ano', fontsize=14, labelpad=20)
axes[1].set_ylabel('Número de Ganhadores', fontsize=14, labelpad=20)
axes[1].set_title('Número de Ganhadores por Ano (5 acertos)', fontsize=16, pad=20)
axes[1].legend()
axes[1].grid(True)
formatter = FuncFormatter(lambda x, pos: '{:.0f}'.format(x))
axes[1].yaxis.set_major_formatter(formatter)

# Gráfico 6 acertos
axes[2].plot(ganhadores_6.index, ganhadores_6.values, marker='o', linestyle='-', label='6 acertos', color='orange')
axes[2].set_xlabel('Ano', fontsize=14, labelpad=20)
axes[2].set_ylabel('Número de Ganhadores', fontsize=14, labelpad=20)
axes[2].set_title('Número de Ganhadores por Ano (6 acertos)', fontsize=16, pad=20)
axes[2].legend()
axes[2].grid(True)
formatter = FuncFormatter(lambda x, pos: '{:.0f}'.format(x))
axes[2].yaxis.set_major_formatter(formatter)
plt.tight_layout()

plt.show()




'''

Gráficos de dispersão entre as bolas sorteadas

'''
plt.figure(figsize=(10, 8))
for i, (bola1, bola2) in enumerate([("N1", "N2"), ("N1", "N3"), ("N1", "N4"), ("N1", "N5"), ("N1", "N6"),
                                    ("N2", "N3"), ("N2", "N4"), ("N2", "N5"), ("N2", "N6"),
                                    ("N3", "N4"), ("N3", "N5"), ("N3", "N6"),
                                    ("N4", "N5"), ("N4", "N6"),
                                    ("N5", "N6")]):
    plt.subplot(4, 4, i + 1)
    plt.scatter(df[bola1], df[bola2], alpha=0.5, edgecolors='w', linewidth=0.5)
    plt.xlabel(bola1, fontsize=5)
    plt.ylabel(bola2, fontsize=5)
    plt.title(f'{bola1} vs {bola2}', fontsize=8)
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
plt.tight_layout(pad=1.0)
plt.suptitle('Gráficos de Dispersão entre as Bolas Sorteadas', y=1.02, fontsize=12)
plt.show()




'''

Histograma do valor dos prêmios de 6 acertos

'''
df['Rateio 6 acertos'] = df["Rateio 6 acertos"].apply(analises.converter_float)
plt.figure(figsize=(14, 7))
plt.hist(df['Rateio 6 acertos'], bins=20, color='yellow', edgecolor='black')
plt.title('Distribuição do Valor dos Prêmios de 6 acertos', fontsize=16, pad=20)
plt.xlabel('Valor do Prêmio', fontsize=14, labelpad=20)
plt.ylabel('Frequência', fontsize=14, labelpad=20)
plt.grid(True)
formatter = FuncFormatter(lambda x, pos: analises.moeda(x))
plt.gca().xaxis.set_major_formatter(formatter)
plt.show()