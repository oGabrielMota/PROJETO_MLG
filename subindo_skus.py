import pandas as pd
from banco_dados import Produtos, session



def subindo_novos_skus():
    nome_arquivo = input("Digite o nome do arquivo de custos atualizados (ex: skus_sem_custo.xlsx): ")
    try:
        df_update = pd.read_excel(nome_arquivo)
        for index, row in df_update.iterrows():
            sku = row['SKU']
            custo = row['custo']

            produto = session.query(Produtos).filter_by(sku=sku).first()
            if produto:
                produto.custo = custo
            else:
                # Se o produto não existe ainda no banco
                novo_produto = Produtos(sku=sku, custo=custo, quantidade_estoque=0)
                session.add(novo_produto)

        session.commit()
        print("Tabela Produtos atualizada com sucesso!")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome e tente novamente.")

