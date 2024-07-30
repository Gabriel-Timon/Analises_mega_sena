### README.md

# Análise e Visualização de Dados da Mega Sena

Este projeto tem como objetivo analisar e visualizar os dados dos sorteios da Mega Sena. Ele inclui um script de análise e um script para gerar gráficos baseados nos resultados das análises. Utilizamos Python, juntamente com as bibliotecas Pandas e Matplotlib, para processar e visualizar os dados.

## Estrutura do Projeto

- `analises.py`: Contém as funções de análise dos dados.
- `all_graphics.py`: Contém a programação para gerar gráficos baseados nas análises.
- `Resultados_Mega.xlsx`: Arquivo Excel com os resultados dos sorteios da Mega Sena.

## Funcionalidades

### Análises realizadas (`analises.py`):

1. **Número total de sorteios**
2. **Quantidade de sorteios com apenas 1 ganhador, mais de 1 e 0 ganhadores**
3. **Os 10 números mais sorteados**
4. **Total de ganhadores de 6, 5 e 4 acertos**
5. **Os 5 estados com mais ganhadores de 6 acertos**
6. **Maior e menor prêmio pago**
7. **O ano com o menor número de ganhadores de 6, 5 e 4 acertos e suas quantidades**
8. **Total pago pela Mega-Sena**

### Gráficos gerados (`all_graphics.py`):

1. **Gráfico de relação de ganhadores e não ganhadores de 6 acertos**
2. **Gráfico do total de sorteios de 4, 5 e 6 acertos**
3. **Gráfico dos 10 números mais sorteados**
4. **Gráficos dos 5 estados mais sorteados**
5. **Gráfico de comparação de 4, 5 e 6 acertos durante os anos**
6. **Gráficos de dispersão entre as bolas sorteadas**
7. **Histograma do valor dos prêmios de 6 acertos**

## Como Executar

1. Certifique-se de ter Python instalado em sua máquina.
2. Instale as dependências necessárias:
    ```bash
    pip install pandas matplotlib openpyxl
    ```
3. Baixe ou clone este repositório.
4. Coloque o arquivo `Resultados_Mega.xlsx` na pasta apropriada.
5. Execute o script de análise:
    ```bash
    python analises.py
    ```
6. Execute o script de geração de gráficos:
    ```bash
    python all_graphics.py
    ```

## Exemplo de Uso

### Script de Análise

```python
if __name__ == "__main__":
    file = "Caminho/para/Resultados_Mega.xlsx"
    df = carregar_dados(file)

    # Número total de sorteios
    print(total_sorteios(df))

    # Quantidade de sorteios com apenas 1 ganhador, mais de 1 e 0 ganhadores
    print(sorteios_ganhadores(df))

    # Os 10 números mais sorteados
    print(numeros_mais_sorteados(df))

    # Total de ganhadores de 6, 5 e 4 acertos
    print(total_ganhadores(df))

    # Os 5 estados com mais ganhadores de 6 acertos
    print(estados_mais_ganhadores(df))

    # Maior e menor prêmio pago
    print(maior_menor_premio(df))

    # O ano com o menor número de ganhadores de 6, 5 e 4 acertos e suas quantidades
    print(ano_menor_ganhadores(df))

    # Total pago pela Mega-Sena
    print(total_pago(df))
```

### Script de Geração de Gráficos

```python
import analises
import matplotlib.pyplot as plt

file = "Caminho/para/Resultados_Mega.xlsx"
df = analises.carregar_dados(file)

# Exemplo de gráfico
sorteios_1ganhador, mais_ganhadores, ninguem = analises.sorteios_ganhadores(df)
plt.bar(['1 Ganhador', 'Mais de 1 Ganhador', 'Zero ganhadores'], [sorteios_1ganhador, mais_ganhadores, ninguem])
plt.show()
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões, melhorias ou correções.

## Licença

Este projeto está licenciado sob a licença MIT.

---

Este projeto é um exemplo de como utilizar Python para análise e visualização de dados, aplicado aos resultados da Mega Sena. Se tiver dúvidas ou sugestões, entre em contato!