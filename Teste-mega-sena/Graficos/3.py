import analises
import matplotlib.pyplot as plt
import numpy as np

file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)


# Gráfico dos 10 números mais sorteados
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