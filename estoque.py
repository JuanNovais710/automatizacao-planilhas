import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta, time

# Lista de produtos em ordem alfabética
import random

produtos = [
    ("ACET CIPROT+ETINILESTRADIOL 2MG+0,035MG C/21 CPR REV(G) CIFARMA", "2200325", "CIFARMA GENERICO", "19,61", random.randint(1, 100)),
    ("ACET CIPROT+ETINILESTRADIOL 2MG+0,035MG C/63 CPR REV(G) CIFARMA", "1091718", "CIFARMA GENERICO", "42,2", random.randint(1, 100)),
    ("ACICLOVIR 200MG C/25 CPR(G) CIFARMA", "1091868", "CIFARMA GENERICO", "75,43", random.randint(1, 100)),
    ("ACICLOVIR CRM 50MG 10G(G) CIFARMA", "1091894", "CIFARMA GENERICO", "24,94", random.randint(1, 100)),
    ("ALGESTONA ACET+ENANTATO ESTRADIOL 150MG+10MG 1AMP 1ML(G) CIFARMA", "1091834", "CIFARMA GENERICO", "12,22", random.randint(1, 100)),
    ("BENATUX C/12 PAST MENTA", "1007236", "CIFARMA GENERICO", "17,25", random.randint(1, 100)),
    ("CIPIONATO TESTOSTERONA 200MG 3AMP 2ML INJ(G) (C5) CIFARMA", "1092392", "CIFARMA GENERICO", "134,1", random.randint(1, 100)),
    ("CYFENOL BABY 100MG 15ML CEREJA", "1091839", "CIFARMA GENERICO", "23,22", random.randint(1, 100)),
    ("DESLORATADINA 0,5MG 100ML(G) CIFARMA", "1091629", "CIFARMA GENERICO", "46,34", random.randint(1, 100)),
    ("DESLORATADINA 0,5MG 60ML(G) CIFARMA", "1091628", "CIFARMA GENERICO", "32,35", random.randint(1, 100)),
    ("DESLORATADINA 1,25MG 20ML(G) CIFARMA", "1092426", "CIFARMA GENERICO", "24,61", random.randint(1, 100)),
    ("DESLORATADINA 5MG C/10 CPR REV(G) CIFARMA", "1091634", "CIFARMA GENERICO", "40,43", random.randint(1, 100)),
    ("DESLORATADINA 5MG C/30 CPR REV(G) CIFARMA", "1091636", "CIFARMA GENERICO", "62,78", random.randint(1, 100)),
    ("ENAN. NORETISTERONA 50MG/ML+ VAL. ESTRADIOL 5MG/ML X 1ML", "1091948", "CIFARMA GENERICO", "16,36", random.randint(1, 100)),
    ("ENANTATO NORETISTERONA+VAL ESTRADIOL 50MG+5MG INJ 1ML+SERINGA(G) CIFARMA MABRA", "1091895", "CIFARMA GENERICO", "21,45", random.randint(1, 100)),
    ("GESTODENO+ETINILESTRADIOL 0,075MG+0,03MG C/21 CPR REV(G) CIFARMA", "1091144", "CIFARMA GENERICO", "30,27", random.randint(1, 100)),
    ("LEVONORGESTREL 1,5MG C/1 CPR(G) CIFARMA", "1091847", "CIFARMA GENERICO", "16,06", random.randint(1, 100)),
    ("LEVONORGESTREL+ETINIL 0,15MG+0,03MG C/21 CPR REV(G) CIFARMA", "1091726", "CIFARMA GENERICO", "6,36", random.randint(1, 100)),
    ("LEVONORGESTREL+ETINIL 0,15MG+0,03MG C/63 CPR REV(G) CIFARMA", "1091727", "CIFARMA GENERICO", "16,46", random.randint(1, 100)),
    ("NIMESULIDA 100MG C/12 CPR DISP(G) CIFARMA", "1091683", "CIFARMA GENERICO", "23,49", random.randint(1, 100)),
    ("OMEPRAZOL 20MG C/90 CPS DURA LIB RETARDADA(G) CIFARMA", "1091006", "CIFARMA GENERICO", "28,96", random.randint(1, 100)),
    ("ORALDRAT 18 ENV 28,8G AGUA DE COCO", "1091975", "CIFARMA GENERICO", "140,47", random.randint(1, 100)),
    ("ORALDRAT 18 ENV 28,8G GUARANA", "1091978", "CIFARMA GENERICO", "140,47", random.randint(1, 100)),
    ("ORALDRAT 18 ENV 28,8G LARANJA", "1091977", "CIFARMA GENERICO", "140,47", random.randint(1, 100)),
    ("ORALDRAT 18 ENV 28,8G NATURAL", "1091976", "CIFARMA GENERICO", "140,47", random.randint(1, 100)),
    ("TENOXICAM 20MG C/10 CPR REV(G) CIFARMA", "1090884", "CIFARMA GENERICO", "39,39", random.randint(1, 100))
]

# Criar planilha com as seguintes colunas
df = pd.DataFrame(produtos, columns=["produto", "id", "laboratório", "preçoBase", "estoque"])

# Adicionar as novas colunas com valores aleatórios
#df['preçoProduto'] = np.round(np.random.uniform(1, 150, size=len(df)), 2)
df['qtdVendas'] = np.random.randint(0, 16, size=len(df))

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
df['dataVenda'] = [random_date_with_time(datetime(2025, 1, 1), datetime(2025, 12, 31)) for _ in range(len(df))]

# Ordenar por nome do produto
df_sorted = df.sort_values(by="produto")

# Salvar como xlsx para Excel
df_sorted.to_excel("estoque_ordenado.xlsx", index=False)

# Imprimir o DataFrame ordenado no console
print(df_sorted)