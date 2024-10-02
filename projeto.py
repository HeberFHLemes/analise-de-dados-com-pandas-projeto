# pip install pandas
# pip install openpyxl
# pip install plotly nbformat
# Analisar dados com pandas, mais operações em "anotacoes.ipynb"

import pandas as pd

dados = pd.read_excel("vendas3.xlsx")

dados_agrupados = dados.groupby(["estado","cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()

dados_agrupados.to_excel("Faturamento.xlsx")

# Confecção de gráficos (em html) sobre os dados obtidos usando plotly.express.
import plotly.express as px

lista_colunas = ["loja", "cidade","estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna,
                           y="preco", 
                           text_auto=True,
                           title="Faturamento",
                           color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Faturamento-{coluna}.html")