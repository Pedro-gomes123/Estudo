import pandas as pd
import sqlite3

conexao = sqlite3.connect("Chinook_Sqlite.sqlite")

# 1. Carregando a Tabela de Vendas (Só tem ID do cliente e Valor)
df_vendas = pd.read_sql_query("SELECT CustomerId, Total, InvoiceDate FROM Invoice", conexao)

# 2. Carregando a Tabela de Clientes (Só tem ID e Nome)
df_clientes = pd.read_sql_query("SELECT CustomerId, FirstName, LastName, Country FROM Customer", conexao)

conexao.close()

print("--- Tabela Vendas (Primeiras linhas) ---")
print(df_vendas.head(3))
print("\n--- Tabela Clientes (Primeiras linhas) ---")
print(df_clientes.head(3))

# ==========================================
# 🛑 O DESAFIO (NÍVEL 2)
# ==========================================

print("\n--- 3. Fazendo o MERGE (O Cruzamento) ---")
# O comando é: pd.merge(tabela_esquerda, tabela_direita, on='Coluna_Em_Comum')
# Tente preencher:
# df_completo = pd.merge(df_vendas, df_..., on='...')

df_completo = pd.merge(df_vendas, df_clientes, left_on='CustomerId', right_on='CustomerId') 
print(df_completo.head(5))
# Se der certo, o df_completo vai ter o valor da venda E o nome do cliente na mesma linha.
# print(df_completo.head())

print("\n--- 4. A Pergunta de Negócio ---")
# Qual foi a MAIOR venda única registrada (Valor máximo)? E quem foi o cliente?
# Dica: Ordene df_completo pelo 'Total' e pegue o topo.
Maior_venda = df_completo.sort_values(by='Total', ascending=False)

print(Maior_venda)