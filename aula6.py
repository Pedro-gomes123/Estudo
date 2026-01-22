import pandas as pd
import sqlite3

# 1. Conexão
conexao = sqlite3.connect("Chinook_Sqlite.sqlite")

# ==========================================
# PARTE 1: EXTRAÇÃO (SQL)
# Escreva as queries para trazer APENAS as colunas necessárias descritas no checklist.
# ==========================================

print("--- 1. Extraindo Dados ---")

# Tabela de Vendas (Dinheiro)
# Dica: SELECT ... FROM Invoice
query_vendas = "..." 
df_vendas = pd.read_sql_query(query_vendas, conexao)

# Tabela de Clientes (A Ponte)
# Dica: SELECT ... FROM Customer
query_clientes = "..."
df_clientes = pd.read_sql_query(query_clientes, conexao)

# Tabela de Funcionários (Os Vendedores)
# Dica: SELECT ... FROM Employee
# Sugestão: Renomeie o FirstName para Nome_Vendedor no SQL (as ...) para facilitar
query_func = "..."
df_func = pd.read_sql_query(query_func, conexao)

conexao.close() # Boa prática: fechar a conexão logo após extrair

# ==========================================
# PARTE 2: ENGENHARIA DE DADOS (PANDAS MERGE)
# Agora vamos costurar as 3 tabelas em uma só.
# ==========================================

print("\n--- 2. Cruzando Tabelas ---")

# PASSO A: Vendas + Clientes
# Use a coluna 'CustomerId' que existe nas duas
# df_passo1 = pd.merge(..., ..., on='...')
df_passo1 = ...

# PASSO B: Resultado Anterior + Funcionários
# CUIDADO:
# Na tabela de clientes (df_passo1) a coluna chama 'SupportRepId'
# Na tabela de funcionários (df_func) a coluna chama 'EmployeeId'
# Use left_on='...' e right_on='...'
# df_completo = pd.merge(..., ..., left_on='...', right_on='...')
df_completo = ...

# Checkpoint: Se der certo, mostra as primeiras linhas
# print(df_completo.head())

# ==========================================
# PARTE 3: ANÁLISE DE NEGÓCIO (GROUPBY)
# Responda as perguntas do Diretor Comercial
# ==========================================

print("\n--- 3. Relatório de Performance ---")

print(">>> RANKING 1: Quem vendeu mais (R$)?")
# Agrupe pelo Nome do Vendedor, some o Total e ordene do maior para o menor
# top_faturamento = ...
# print(top_faturamento)

print("\n>>> RANKING 2: Quem trabalhou mais (Quantidade de Vendas)?")
# Agrupe pelo Nome do Vendedor e CONTE quantas vendas ele fez (count)
# top_esforco = ...
# print(top_esforco)