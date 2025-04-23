import pandas as pd

#lê planilha
df = pd.read_excel('Estudo_de_Caso_PGFN.xlsx')

quantidade_mulheres = df[df['codsexo'] == 'F'].shape[0]  

print(f'Total de mulheres: {quantidade_mulheres}')