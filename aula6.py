import pandas as pd
import sqlite3

conexao = sqlite3.connect("Chinook_Sqlite.sqlite")

# ==============================================================================
# 1. EXTRAÇÃO (SQL)
# Precisamos de 3 tabelas. Cuidado com nomes de colunas repetidos (Name)!
# ==============================================================================

print("--- 1. Buscando dados Brutos ---")

# TABELA A: Itens da Fatura (InvoiceLine)
# Precisamos saber o ID da música (TrackId), o Preço (UnitPrice) e a Quantidade (Quantity)
# Dica: SELECT ... FROM InvoiceLine
query_itens = " SELECT TrackId, UnitPrice, Quantity FROM InvoiceLine; "
df_itens = pd.read_sql_query(query_itens, conexao)

# TABELA B: Músicas (Track)
# Precisamos do ID da música (TrackId), do Nome da Música (Name) e do ID do Gênero (GenreId)
# Dica: SELECT ... FROM Track
query_tracks = " SELECT TrackId , Name, GenreId FROM Track;"
df_tracks = pd.read_sql_query(query_tracks, conexao)

# TABELA C: Gêneros (Genre)
# Precisamos do ID (GenreId) e do Nome do Gênero (Name)
# Dica Importante: No SQL, renomeie a coluna Name para 'Nome_Genero' (usando AS)
# para não confundir com o nome da música depois.
query_genres = " SELECT GenreID, Name AS Nome_Genero FROM Genre; "
df_genres = pd.read_sql_query(query_genres, conexao)

conexao.close()

# ==============================================================================
# 2. ENGENHARIA DE DADOS (Cálculos + Merges)
# ==============================================================================

print("\n--- 2. Tratando os Dados ---")

# PASSO A: Criar Coluna de Faturamento Total por Item
# No Pandas, multiplique a coluna UnitPrice pela coluna Quantity dentro do df_itens


df_itens['Total Vendido'] = df_itens['UnitPrice'] * df_itens['Quantity']
print(df_itens)

# PASSO B: Primeiro Merge (Itens + Músicas)
# Junte df_itens com df_tracks usando a chave 'TrackId'

df_marge1 = pd.merge(df_itens, df_tracks, left_on='TrackId', right_on='TrackId')
print(df_marge1)

# PASSO C: Segundo Merge (Resultado + Gêneros)
# Junte df_merge1 com df_genres usando a chave 'GenreId'

df_final = pd.merge(df_marge1, df_genres, left_on='GenreId', right_on='GenreId')
print(df_final)




# ==============================================================================
# 3. INTELIGÊNCIA DE MERCADO (Análise)
# ==============================================================================

print("\n--- PERGUNTA 1: Qual Gênero dá mais Lucro? ---")
# Agrupe df_final por 'Nome_Genero', some a coluna 'Total_Item' e ordene (desc).
Lucro = df_final.groupby('Nome_Genero')['Total Vendido'].sum().sort_values(ascending=False)
print(Lucro)


print("\n--- PERGUNTA 2: Drill-Down (Aprofundamento) ---")
# Agora que você sabe qual é o Gênero nº 1 (provavelmente Rock ou Latin),
# Crie um filtro para pegar APENAS as vendas desse gênero específico.
# df_top_genero = df_final[df_final['Nome_Genero'] == 'Nome Do Genero Campeao']

print("--- Dentro do Gênero Campeão, qual a música mais vendida? ---")
# Agrupe esse df filtrado (df_top_genero) pelo nome da música ('Name'),
# some o 'Total_Item' e mostre a campeã.
# top_musica = ...
# print(top_musica.head(1))