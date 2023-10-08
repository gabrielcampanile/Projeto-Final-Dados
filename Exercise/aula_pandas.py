# -*- coding: utf-8 -*-
"""Aula_Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13bCm22pFcqm2Ezovk6Ra0-Srq7aBWSgU
"""

import pandas as pd

"""Criando um dataframe a partir de um dicionário"""

#dataframe = pd.DataFrame()
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijão', 'arroz'],
         'qtde': [50, 70],
         }
#tabela vendas
vendas_df = pd.DataFrame(venda)

"""Visualização dos Dados


*   print
*   display


"""

print(vendas_df)

display(vendas_df)

"""Importando arquivos e bases de dados"""

vendas_df = pd.read_excel('Vendas.xlsx')
display(vendas_df)

"""Resumos de Visualização de Dados simples e úteis
*   head
*   shape
*   describe


"""

display(vendas_df.head(10))

print(vendas_df.shape)

display(vendas_df.describe())

"""Pegar 1 coluna (e os pd.Series)
 -1 coluna (série)
 -2 ou + colunas (tabela)
"""

produtos = vendas_df[['Produto', 'ID Loja']]
display(produtos)

""".loc, um método muito importante
*   pegar 1 linha  
*   pegar linhas de acordo com alguma condição
*   pegar linhas e colunas específicas
*   pegar 1 valor específico
"""

#pegar uma linha
display(vendas_df.loc[1])

#pegar várias linhas
display(vendas_df.loc[1:5])

#pegar linhas que correspondem a uma condição
#.loc[coluna]
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']
display(vendas_norteshopping_df)

#pegar várias linhas e colunas usando loc
#.loc[linhas, colunas]
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
display(vendas_norteshopping_df)

#pegar um valor específico
print(vendas_df.loc[1, 'Produto'])

"""Adicionar 1 coluna"""

#a partir de uma coluna que já existe
vendas_df['Comissão'] = vendas_df['Valor Final'] * 5 / 100
display(vendas_df)

#criar uma coluna com valor padrão
#vendas_df['Imposto'] = 0
#.loc[linha, coluna]
vendas_df.loc[:, 'Imposto'] = 2
display(vendas_df)

"""Adicionar 1 linha
  - linhas de um complemento da base de dados
"""

vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
display(vendas_dez_df)

vendas_df = vendas_df.append(vendas_dez_df)
display(vendas_df)

"""Excluir linhas e colunas"""

#vendas_df = vendas_df.drop('Imposto', axis=1)
vendas_df = vendas_df.drop(0, axis=0)
display(vendas_df)

"""Valores Vazios
- deletar linhas/colunas vazias
- deletar linhas que possuem valores vazios
- preencher valores vazios (média e último valor)
"""

#deletar linhas e colunas completamente vazias
vendas_df = vendas_df.dropna(how='all', axis=1)

#deletar linhas que possuem pelo menos um valor vazio
vendas_df = vendas_df.dropna()

#preencher valores vazios
#1-preencher com a média da coluna --- .mean()
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
display(vendas_df)

#2-preencher com o último valor
vendas_df = vendas_df.ffill()

"""Calcular Indicadores
- Groupby
- Value Counts
"""

#sum() somar
#mean() média
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').mean()
display(faturamento_produto)

transacoes_loja = vendas_df['ID Loja'].value_counts()
print(transacoes_loja)

"""Mesclar 2 dataframes (Procurar informações de um dataframe em outro)"""

gerentes_df = pd.read_excel('Gerentes.xlsx')
#display(gerentes_df)

vendas_df = vendas_df.merge(gerentes_df)
display(vendas_df)