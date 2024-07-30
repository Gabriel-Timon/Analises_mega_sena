import analises
import matplotlib.pyplot as plt
import numpy as np

file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)


# Gráfico do total de sorteios de 4, 5 e 6 acertos
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