import pandas as pd
import sqlite3
import os

# Nome do arquivo
nome_banco = "Chinook_Sqlite.sqlite"

# --- 1. VERIFICAÇÃO ---
print(f"📂 Abrindo arquivo: {nome_banco}")
if not os.path.exists(nome_banco):
    print("❌ ERRO: O arquivo sumiu! Rode o script de download novamente.")
    exit()

# --- 2. DESCOBRINDO O NOME DAS TABELAS ---
conexao = sqlite3.connect(nome_banco)
cursor = conexao.cursor()

# Pede pro banco listar todas as tabelas que existem nele
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("\n📋 Tabelas encontradas no banco:")
# Limpa a visualização para mostrar só os nomes
nomes_tabelas = [tabela[0] for tabela in tabelas]
print(nomes_tabelas)

# --- 3. QUERY CORRIGIDA (SINGULAR) ---
# Note: Mudei de 'customers' para 'Customer' e 'invoices' para 'Invoice'
query = """
SELECT 
    c.FirstName || ' ' || c.LastName as Cliente,
    c.Country as Pais,
    i.InvoiceDate as Data,
    i.Total as Valor
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
LIMIT 20
"""

try:
    print("\n🚀 Rodando a Análise...")
    df = pd.read_sql_query(query, conexao)
    print("✅ SUCESSO! Dados carregados:")
    print(df)
except Exception as e:
    print(f"❌ Erro na query: {e}")

conexao.close()