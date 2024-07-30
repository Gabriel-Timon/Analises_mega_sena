# Análises da planilha da Mega Sena. Análises:

'''

1. Número total de sorteios
2. Quantidade de sorteios com apenas 1 ganhador, mais de 1 e 0 ganhadores
3. Os 10 números mais sorteados
4. Total de ganhadores de 6, 5 e 4 acertos
5. Os 5 estados com mais ganhadores de 6 acertos
6. Maior e menor prêmio pago
7. O ano com o menor número de ganhadores de 6, 5 e 4 acertos e suas quantidades
8. Total pago pela Mega-Sena

'''

import pandas as pd
from collections import Counter
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def titulo(msg):
    print(msg)
    print('-' * (len(msg) + 3))


def moeda(valor):
    return locale.currency(valor, grouping=True)


def converter_float(valor):
    valor = valor.replace('R$', '').replace('.', '').replace(',', '.')
    try:
        return float(valor)
    except ValueError:
        return 0.0


def carregar_dados(file):
    df = pd.read_excel(file)
    df.drop('Observação', axis=1, inplace=True)
    df.drop('Arrecadação Total', axis=1, inplace=True)
    df.drop('Estimativa prêmio', axis=1, inplace=True)
    df.drop('Acumulado Sorteio Especial Mega da Virada', axis=1, inplace=True)
    df.rename(columns={
        'Concurso': 'ID',
        'Data do Sorteio': 'Data',
        'Bola1': 'N1',
        'Bola2': 'N2',
        'Bola3': 'N3',
        'Bola4': 'N4',
        'Bola5': 'N5',
        'Bola6': 'N6',
        'Ganhadores 6 acertos': '6 acertos',
        'Cidade / UF': 'UF',
        'Ganhadores 5 acertos': '5 acertos',
        'Ganhadores 4 acertos': '4 acertos'
    }, inplace=True)
    df = df.fillna(0)
    return df


def total_sorteios(df):
    return len(df)


def sorteios_ganhadores(df):
    sorteios_1ganhador = df[df['6 acertos'] == 1].shape[0]
    mais_ganhadores = df[df['6 acertos'] > 1].shape[0]
    ninguem = df[df['6 acertos'] == 0].shape[0]
    return sorteios_1ganhador, mais_ganhadores, ninguem


def numeros_mais_sorteados(df):
    numeros_sorteados = df[["N1", "N2", "N3", "N4", "N5", "N6"]]
    numeros_flat = numeros_sorteados.values.flatten()
    contador_numeros = Counter(numeros_flat)
    mais_sorteados = contador_numeros.most_common(10)
    return mais_sorteados


def total_ganhadores(df):
    total_ganhadores_6_acertos = df['6 acertos'].sum()
    total_ganhadores_5_acertos = df['5 acertos'].sum()
    total_ganhadores_4_acertos = df['4 acertos'].sum()
    return total_ganhadores_6_acertos, total_ganhadores_5_acertos, total_ganhadores_4_acertos


def estados_mais_ganhadores(df):
    df['Estado'] = df['UF'].apply(lambda x: str(x)[-2:] if pd.notna(x) else 'Desconhecido')
    estados_ganhadores = df[df['Estado'] != 'Desconhecido']['Estado'].value_counts().head(6)[1:6]
    lst_estados_ganhadores = list(estados_ganhadores.items())
    return lst_estados_ganhadores

def maior_menor_premio(df):
    df['Rateio 6 acertos'] = df["Rateio 6 acertos"].apply(converter_float)
    df['Rateio 4 acertos'] = df["Rateio 4 acertos"].apply(converter_float)
    maior_premio = df['Rateio 6 acertos'].max()
    menor_premio = df['Rateio 4 acertos'].min()
    return maior_premio, menor_premio


def ano_menor_ganhadores(df):
    df['Ano'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.year
    ganhadores_por_ano = df.groupby('Ano').agg({
        '6 acertos': 'sum',
        '5 acertos': 'sum',
        '4 acertos': 'sum'
    }).reset_index().sort_values('6 acertos')
    ano_menor_ganhadores_6_acertos = ganhadores_por_ano.loc[ganhadores_por_ano['6 acertos'].idxmin()]
    return dict(ano_menor_ganhadores_6_acertos)


def total_pago(df):
    soma_4 = df["Rateio 4 acertos"].sum()
    soma_5 = df["Rateio 5 acertos"].apply(converter_float).sum()
    soma_6 = df["Rateio 6 acertos"].sum()
    total_pago = soma_4 + soma_5 + soma_6
    return soma_4, soma_5, soma_6, total_pago

# Exemplo de uso
if __name__ == "__main__":
    file = "C:/Users/radar/OneDrive/Área de Trabalho/Teste-mega-sena/Arquivos/Resultados_Mega.xlsx"
    df = carregar_dados(file)
    

    # 1. Número total de sorteios
    titulo('Número total de sorteios')
    print(f'\033[32m{total_sorteios(df)}\033[m sorteios\n\n\n\n')



    # 2. Quantidade de sorteios com apenas 1 ganhador, mais de 1 e 0 ganhadores
    titulo('Quantidade de sorteios com apenas 1 ganhador, mais de 1 e 0 ganhadores')
    sorteios_1ganhador, mais_ganhadores, ninguem = sorteios_ganhadores(df)
    print(f'Zero ganhadores: \033[32m{ninguem}\033[m sorteios')
    print(f'Mais de um ganhador: \033[32m{mais_ganhadores}\033[m sorteios')
    print(f'Apenas um ganhador: \033[32m{sorteios_1ganhador}\033[m sorteios\n\n\n\n')



    # 3. Os 10 números mais sorteados
    titulo('Os 10 números mais sorteados')
    for numero, frequencia in numeros_mais_sorteados(df):
        print(f"Número {numero}: \033[32m{frequencia}\033[m vezes")
    print('\n\n\n')




    # 4. Total de ganhadores de 6, 5 e 4 acertos
    titulo('Total de ganhadores de 6, 5 e 4 acertos')
    total_ganhadores_6_acertos, total_ganhadores_5_acertos, total_ganhadores_4_acertos = total_ganhadores(df)
    print(f'6 acertos: \033[32m{total_ganhadores_6_acertos}\033[m ganhadores')
    print(f'5 acertos: \033[32m{total_ganhadores_5_acertos}\033[m ganhadores')
    print(f'4 acertos: \033[32m{total_ganhadores_4_acertos}\033[m ganhadores\n\n\n\n')



    # 5. Os 5 estados com mais ganhadores de 6 acertos
    titulo('Os 5 estados com mais ganhadores de 6 acertos')
    for estados, quantidade in estados_mais_ganhadores(df):
        print(f'{estados}: \033[32m{quantidade}\033[m vezes')
    print('\n\n\n')



    # 6. Maior e menor prêmio pago
    titulo('Maior e menor prêmio pago')
    maior_premio, menor_premio = maior_menor_premio(df)
    print(f'Maior prêmio: \033[32m{moeda(maior_premio)}\033[m')
    print(f'Menor prêmio: \033[32m{moeda(menor_premio)}\033[m\n\n\n\n')



    # 7. O ano com o menor número de ganhadores de 6, 5 e 4 acertos e suas quantidades
    titulo('O ano com o menor número de ganhadores de 6, 5 e 4 acertos')
    result = ano_menor_ganhadores(df)
    print(f'Ano: {result["Ano"]}\n'
          f'6 acertos: \033[32m{result["6 acertos"]}\033[m ganhadores\n'
          f'5 acertos: \033[32m{result["5 acertos"]}\033[m ganhadores\n'
          f'4 acertos: \033[32m{result["4 acertos"]}\033[m ganhadores\n\n\n\n')


    # 8. Total pago pela Mega-Sena
    titulo('Total pago pela Mega-Sena')
    soma_4, soma_5, soma_6, total_pago = total_pago(df)
    print(f'Total pago para ganhadores com:\n'
          f'6 acertos: \033[32m{moeda(soma_6)}\033[m\n'
          f'5 acertos: \033[32m{moeda(soma_5)}\033[m\n'
          f'4 acertos: \033[32m{moeda(soma_4)}\033[m\n'
          f'Total: \033[32m{moeda(total_pago)}\033[m\n')
