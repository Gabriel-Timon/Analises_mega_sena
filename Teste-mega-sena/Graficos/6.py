import pandas as pd
import matplotlib.pyplot as plt
import analises
import seaborn as sns
from collections import Counter

file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)



# Gráficos de dispersão entre as bolas sorteadas
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