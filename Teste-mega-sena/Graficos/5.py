import matplotlib.pyplot as plt
import numpy as np
import analises

file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)

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
