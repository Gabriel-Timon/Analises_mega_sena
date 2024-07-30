import pandas as pd
import matplotlib.pyplot as plt
import analises
import seaborn as sns
from collections import Counter
from matplotlib.ticker import FuncFormatter
import locale


file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)


df['Rateio 6 acertos'] = df["Rateio 6 acertos"].apply(analises.converter_float)

# Histograma do valor dos prêmios de 6 acertos
plt.figure(figsize=(14, 7))
plt.hist(df['Rateio 6 acertos'], bins=20, color='yellow', edgecolor='black')
plt.title('Distribuição do Valor dos Prêmios de 6 acertos', fontsize=16, pad=20)
plt.xlabel('Valor do Prêmio', fontsize=14, labelpad=20)
plt.ylabel('Frequência', fontsize=14, labelpad=20)
plt.grid(True)
formatter = FuncFormatter(lambda x, pos: analises.moeda(x))
plt.gca().xaxis.set_major_formatter(formatter)
plt.show()