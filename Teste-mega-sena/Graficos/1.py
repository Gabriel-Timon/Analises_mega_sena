import analises
import matplotlib.pyplot as plt
import numpy as np


file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)



# Gráfico de relação de ganhadores e não ganhadores de 6 acertos
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