import pandas as pd
import numpy as np

dados = {
    'Data': ['2024-01-15', '15/01/2024', '2024-01-16', '2024-01-16', None, '2024-01-17'],
    'Vendedor': ['João', 'Joao', 'Maria', 'MARIA', 'Carlos', 'João'],
    'Produto': ['Teclado', 'Mouse', 'Monitor', 'Teclado', 'Mouse', 'Monitor'],
    'Valor': ['150', '50', '1200', '150', None, '1200'],
    'Quantidade': [2, 5, 1, 3, 2, 1],
    'Região': ['PE', 'PE', 'SP', 'SP', 'RJ', 'PE']
}

df = pd.DataFrame(dados)

# --- TRATAMENTO CORRIGIDO ---

# 1. Converter para Numérico (A forma mais segura)
# 'coerce' força erros (como texto ou None) a virarem NaN (Not a Number)
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

# 2. Preencher os nulos com 0 (para poder multiplicar depois)
df['Valor'] = df['Valor'].fillna(0)

# 3. Padronizar Vendedores
# .str.title() resolve MARIA -> Maria, mas Joao (sem acento) continua diferente de João
df['Vendedor'] = df['Vendedor'].str.title().replace('Joao', 'João')

# 4. Limpar datas vazias
df = df.dropna(subset=['Data'])

# 5. Calcular Total (Agora funciona porque Valor é número)
df['Total Vendas'] = df['Valor'] * df['Quantidade']

# 6. Agrupar e MOSTRAR (precisa do print)
resultado = df.groupby('Vendedor')['Total Vendas'].mean()

print("--- Tabela Tratada ---")
print(df)
print("\n--- Média por Vendedor ---")
print(resultado)
print("\n--- Tipos de Dados ---")
print(df.dtypes)