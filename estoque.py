import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta, time

# Caminho da planilha a ser lida
file_path = "C:\\Users\\user\\Desktop\\marcandoOTempo\\estoquePy\\lists\\NeoQuimica1.xlsx"

# Lista de produtos em ordem alfabética
df = pd.read_excel(file_path, nrows=199)

# Inicializa o array de produtos
produtos = []

# Altera o nome das colunas originais para: "id, produto, laboratorio, preçobase, subgrupo"
df.rename(columns={
        'Cód. Interno': 'id',
        'Produto': 'PRODUTO',
        'Fornecedor': 'LABORATÓRIO',
        'Preço base': 'PREÇO-BASE',
        'Sub-Grupo': 'SUB-GRUPO'
    }, inplace=True)

# Adicionar as novas colunas com valores aleatórios
df['id'] = ["100" + "".join([str(random.randint(0, 9)) for _ in range(4)]) for _ in range(len(df))]
#df['preçoBase'] = np.random.uniform(10.0, 500.0, size=len(df))
df['ESTOQUE'] = np.random.randint(0, 19999, size=len(df))
df['QUANTIDADE DE VENDAS'] = np.random.randint(0, 500, size=len(df))

# Gerar datas aleatórias para 2025
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# Função retorna um objeto datetime completo
def random_date_with_time(start, end):
    random_day = start + timedelta(days=random.randint(0, (end - start).days))
    random_hour = random.randint(9, 18)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    return random_day.replace(hour=random_hour, minute=random_minute, second=random_second)

# A coluna `dataVenda` recebe o resultado completo da função, com data e hora
df['Data venda'] = [random_date_with_time(datetime(2025, 1, 1), datetime(2025, 12, 31)) for _ in range(len(df))]

# Ordenar por nome do produto
df_sorted = df.sort_values(by="PRODUTO")

# Salvar como xlsx para Excel
df_sorted.to_excel("finalSheet.xlsx", index=False)

# Imprimir o DataFrame ordenado no console
print(df_sorted)