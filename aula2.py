import pandas as pd
import sqlite3

# Conexão
conexao = sqlite3.connect("Chinook_Sqlite.sqlite")

# Trazendo a tabela pronta do SQL
# Note que eu já renomeei as colunas para facilitar sua vida
query = """
SELECT 
    c.FirstName || ' ' || c.LastName as Cliente,
    c.Country as Pais,
    i.InvoiceDate as Data,
    i.Total as Valor
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
"""

df = pd.read_sql_query(query, conexao)
conexao.close()

print("--- DADOS CARREGADOS ---")
# Mostra as primeiras 5 linhas para você ver as colunas: 'Cliente', 'Pais', 'Data', 'Valor'
print(df.head()) 

# ==========================================
# 🛑 DESAFIO COMEÇA AQUI
# ==========================================

print("\n--- MISSÃO 1: Top 5 Países em Vendas ---")
# Dica: Agrupe por 'Pais', some o 'Valor', ordene e pegue os 5 primeiros
# top_paises = df.groupby(...)...
# print(top_paises)
Top_Paises = df.groupby('Pais')['Valor'].sum()
print(Top_Paises)

print("\n--- MISSÃO 2: Cliente VIP do Brasil ---")
# Dica: Primeiro crie um df só com Brasil: df_br = df[df['Pais'] == 'Brazil']
# Depois agrupe por 'Cliente' e some
# vip_br = ...
# print(vip_br)

df_brasil = df[df['Pais'] == 'Brazil']

vip_br = df_brasil.groupby('Cliente')['Valor'].sum()
print(vip_br)

print("\n--- MISSÃO 3: Ticket Médio Geral ---")
# Dica: Qual a média da coluna 'Valor'?
# media = ...
# print(media)

media = df['Valor'].mean()
print(media)