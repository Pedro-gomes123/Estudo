import pandas as pd
import sqlite3

# 1. CONEXÃO
conexao = sqlite3.connect("Chinook_Sqlite.sqlite")

# ==============================================================================
# PASSO 1: SQL (Sua vez)
# ==============================================================================
print("--- 1. Buscando Dados ---")

# REGRAS DO SQL:
# 1. Tabela: Invoice
# 2. Colunas necessárias: InvoiceId e Total
query = "..." # Escreva sua query aqui dentro

# Carregando no Pandas
df = pd.read_sql_query(query, conexao)
conexao.close()

# Mostrando as primeiras linhas para garantir que veio certo
print(df.head())

# ==============================================================================
# PASSO 2: A LÓGICA DO DESCONTO (Sua vez)
# ==============================================================================
print("\n--- 2. Criando a Função de Desconto ---")

def regra_desconto(valor):
    # REGRAS DE NEGÓCIO:
    # 1. Se valor for MAIOR que 10.00 -> Retorne "15% OFF"
    # 2. Se valor for MENOR OU IGUAL a 10.00 E MAIOR OU IGUAL a 5.00 -> Retorne "5% OFF"
    # 3. Qualquer outro caso (menor que 5) -> Retorne "Zero"
    
    # DICA: Use if, elif e else.
    # DICA: Lembre-se de usar 'return' e não 'print'.
    
    pass # Apague este 'pass' e escreva sua lógica aqui

# ==============================================================================
# PASSO 3: APLICANDO NO PANDAS
# ==============================================================================

# Crie uma coluna nova chamada 'Status_Desconto'
# Aplique a função 'regra_desconto' na coluna 'Total'
# df['Status_Desconto'] = ...

print("\n--- Resultado Final ---")
# print(df.head(10))