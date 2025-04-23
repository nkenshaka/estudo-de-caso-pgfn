# Estudo de Caso - PGFN (Ministério da Fazenda)

Este repositório contém a resolução técnica de um estudo de caso proposto pela PGFN (Procuradoria-Geral da Fazenda Nacional) como parte de um processo seletivo para estágio na área de dados e tecnologia.

> ⚠️ **Este projeto foi desenvolvido com fins educacionais e seletivos, sem qualquer vínculo institucional com a PGFN.**  
> Nenhum dado sensível foi exposto. Todos os dados utilizados são de domínio público ou anonimizados.

---

## 📌 Objetivo

Realizar análises e extrações de dados a partir de planilhas Excel, utilizando Python e bibliotecas como pandas e NumPy. O foco está em aplicar lógica, limpeza e automação para transformar dados em insights organizados.

---

## 📁 Estrutura do Projeto

/codigo ├── item1.py → Análise de servidores por região ├── item2.py → Contagem de servidoras do sexo feminino ├── item3.py → Filtragem de situação funcional "DESCENT CARREI" └── item4.py → Cálculo de aposentadoria por idade e sexo
/documentacao └── Estudo_de_Caso_PGFN_Shaka.pdf → Documento completo com lógica, problemas e soluções
/resultado └── Resultado_Aposentadoria.xlsx → Planilha com o resultado final (anonimizada)



---

## 🛠️ Tecnologias Utilizadas

- Python 3.12  
- pandas  
- NumPy  
- openpyxl  

---

## 🔍 Detalhes Técnicos

- Manipulação de planilhas Excel (.xlsx) com múltiplas abas
- Padronização de nomes de colunas
- Merge entre planilhas (join SQL-like com `merge`)
- Limpeza de dados (`dropna`, conversão de tipos)
- Filtragem por strings (`str.contains`)
- Cálculo de idade a partir de datas Excel (`pd.to_datetime`)
- Condicionais (`np.where`) para criação de colunas baseadas em regras
- Exportação de resultados para Excel (`to_excel`)

---

## 🚀 Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/nkenshaka/estudo-de-caso-pgfn.git


