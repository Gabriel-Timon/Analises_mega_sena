import pandas as pd
import matplotlib.pyplot as plt
import analises
from matplotlib.ticker import FuncFormatter

file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)

# Gráfico de Linhas dos Ganhadores ao Longo do Tempo
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