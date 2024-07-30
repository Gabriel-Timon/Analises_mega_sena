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
    estados_ganhadores = df[df['Estado'] != 'Desconhecido']['Estado'].value_counts().head(5)[1:5]
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

