import pandas as pd

# Carregar a planilha
arquivo = 'Estudo_de_Caso_PGFN.xlsx'
df = pd.read_excel(arquivo, sheet_name='Servidores')
df.columns = df.columns.str.lower()

# Filtrar os servidores cuja situação funcional contenha "DESCENT CARREI"
filtro = df[
    df['nomesitfuncional'].astype(str).str.contains('DESCENT CARREI', case=False, na=False)
]

print(f"🔢 Total de servidores com situação funcional que contém 'DESCENT CARREI': {len(filtro)}")
