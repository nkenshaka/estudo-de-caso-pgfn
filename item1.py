import pandas as pd

# Caminho do arquivo
arquivo = 'Estudo_de_Caso_PGFN.xlsx'

# Carrega as planilhas
df_servidores = pd.read_excel(arquivo, sheet_name='Servidores')
df_unidades = pd.read_excel(arquivo, sheet_name='Unidade', skiprows=4)

# Renomeia e seleciona apenas as colunas necessárias
df_unidades = df_unidades.rename(columns={
    'Código UORG': 'codigo_uorg',
    'Região': 'regiao'
})[['codigo_uorg', 'regiao']]

# Remove linhas com valores ausentes nas colunas-chave
df_unidades = df_unidades.dropna(subset=['codigo_uorg', 'regiao'])
df_servidores = df_servidores.dropna(subset=['coduorgexercicio'])

# Converte os códigos para inteiros
df_unidades['codigo_uorg'] = df_unidades['codigo_uorg'].astype(int)
df_servidores['coduorgexercicio'] = df_servidores['coduorgexercicio'].astype(int)

# Faz o merge com base no código da unidade
df_completo = pd.merge(
    df_servidores,
    df_unidades,
    left_on='coduorgexercicio',
    right_on='codigo_uorg',
    how='left'
)

# Conta quantas vezes cada região aparece
contagem = df_completo['regiao'].value_counts()

# Mostra o resultado
print("Contagem de servidores por região:")
print(contagem)
