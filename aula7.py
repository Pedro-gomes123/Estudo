import pandas as pd
import sqlite3

conexao = sqlite3.connect("Chinook_Sqlite.sqlite")

# Trazendo nome da música e duração em milissegundos
# Peguei só 20 músicas para facilitar a visualização
query = "SELECT Name, Milliseconds FROM Track LIMIT 20 "
df = pd.read_sql_query(query, conexao)
conexao.close()

print("--- Dados Originais ---")
print(df.head())

# =======================================================
# 🛑 SUA VEZ: CRIE A LÓGICA AQUI
# =======================================================

def classificar_musica(ms):
    # 1. Converta ms para minutos (divida por 60000)
    # minutos = ...
    minutos = ms / 60000
    
    if minutos >= 5:
        print('Epica')
    elif minutos < 3:
        print('Curta')
    else:
       print('Normal')
    # 2. Escreva o IF / ELIF / ELSE
    # Se minutos >= 5 -> return "Épica"
    # Se minutos < 3 -> return "Curta"
    # Senão -> return "Normal"
    
    # APAGUE ESSE PASS E ESCREVA SEU CÓDIGO
    return 

# =======================================================
# APLICANDO NO PANDAS
# =======================================================

# Aqui aplicamos a SUA função na coluna Milliseconds
df['Categoria'] = df['Milliseconds'].apply(classificar_musica)

print("\n--- Resultado da Classificação ---")
print(df[['Name', 'Milliseconds', 'Categoria']])