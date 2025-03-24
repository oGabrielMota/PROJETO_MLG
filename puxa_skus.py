import pandas as pd
from pathlib import Path
from banco_dados import Produtos, session


arquivo = Path("sku.xlsx")
skus_criados = session.query(Produtos).all()

if arquivo.exists():
    planilha_sku =  pd.read_excel("sku.xlsx")
else:
    planilha_sku =  pd.read_excel("sku_fake.xlsx")


array_skus = planilha_sku.values.tolist()


if len(skus_criados) == 0: 
    for skus in array_skus:
        novo_cadastro = Produtos(
            sku=skus[0],
            custo=skus[1],
            quantidade_estoque= 0
        )
        session.add(novo_cadastro)

session.commit()