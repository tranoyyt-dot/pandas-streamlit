import pandas as pd
dados = {
    "Produto": ["Caneta", "Caderno", "Borracha", "Caneta", "Caderno", "Caneta"],
    "Quantidade": [10, 5, 8, 3, 6, 12],
    "Preço_Unitário": [2.5, 15.0, 1.5, 2.5, 15.0, 2.5]   
}
df = pd.DataFrame(dados)
df["Valor_total"] = df["Quantidade"]*df["Preço_Unitário"]
print(df.head())
resumo = df.groupby("Produto")["Valor_total"].sum().reset_index()
print("Total vendido por produto ")
print(resumo)
df.to_excel("vendas.xlsx", index=False)
resumo.to_excel("resumo.xlsx", index=False)