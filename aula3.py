import pandas as pd
import sqlite3

# Conexão e Query (A mesma de antes)
conexao = sqlite3.connect("Chinook_Sqlite.sqlite")
query = """
SELECT 
    i.InvoiceDate as Data,
    i.Total as Valor
FROM Invoice i
"""
df = pd.read_sql_query(query, conexao)
conexao.close()

# --- 🛑 AQUI COMEÇA O NÍVEL 2 ---

print("--- 1. Verificando o Tipo Original ---")
print(df.info()) 
# (Note que 'Data' vai aparecer como 'object', que é texto no Pandas)


print("\n--- 2. Convertendo para Data ---")
# COMANDO NOVO: pd.to_datetime()
# Preencha: df['Data'] = pd.to_datetime(df['...'])
df['Data'] = pd.to_datetime(df['Data']) 
print(df.info())

print("\n--- 3. Criando a Coluna Ano ---")
# Quando a coluna já é data, podemos usar o acessador .dt
# Exemplo: df['Data'].dt.month (pega o mês), df['Data'].dt.day (pega o dia)
# MISSÃO: Crie a coluna 'Ano' pegando o .year
df['Ano'] = df['Data'].dt.year


print(df.info())
print("\n--- 4. Vendas por Ano ---")
# MISSÃO: Agrupe por 'Ano', some o 'Valor' e ordene
vendas_ano = df.groupby('Ano')['Valor'].sum().sort_values(ascending=False )
print(vendas_ano)
# print(vendas_ano)

df['Mês'] = df['Data'].dt.month
Vendas_mes = df.groupby('Mês')['Valor'].sum().sort_values(ascending=False)
print(Vendas_mes)