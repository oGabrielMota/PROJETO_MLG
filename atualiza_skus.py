import pandas as pd
from banco_dados import Conteudo_Relatorio, Produtos, session

def atualizar_custos():

    conteudos = session.query(Conteudo_Relatorio).all()
    
    skus_sem_custo = []
    skus_nao_cadastrados = []

    for conteudo in conteudos:
        sku = conteudo.sku
        
    
        produto = session.query(Produtos).filter_by(sku=sku).first()

        if produto:
            if produto.custo == 0:  # Se custo é zero, atualiza
                conteudo.lucro_liquido = conteudo.valor_venda - produto.custo
            else:
                conteudo.lucro_liquido = conteudo.valor_venda - produto.custo
        else:
            # Se não tem o SKU cadastrado, adiciona à lista
            skus_nao_cadastrados.append(sku)

            # Se não tiver custo, adiciona à lista de SKUs sem custo
            if conteudo.lucro_liquido == 0:
                skus_sem_custo.append(sku)


    session.commit()

    # Se houver SKUs sem custo ou não cadastrados, pede pro usuário subir um arquivo
    if skus_sem_custo or skus_nao_cadastrados:
        print(f"SKUs sem custo: {len(skus_sem_custo)}")
        print(f"SKUs não cadastrados: {len(skus_nao_cadastrados)}")

        # Se tiver SKUs sem custo, pede ao usuário para enviar o arquivo com os custos
        if skus_sem_custo:
            print(f"SKUs sem custo: {skus_sem_custo}")
            resposta = input("Deseja adicionar os custos? Envie o arquivo com o custo dos SKUs (s/n): ").lower()
            if resposta == "s":
                nome_arquivo = input("Digite o nome do arquivo com os custos (ex: skus_sem_custo.xlsx): ")

                try:
                    df_update = pd.read_excel(nome_arquivo)
                    for index, row in df_update.iterrows():
                        sku = row['SKU']
                        custo = row['custo']

                        produto = session.query(Produtos).filter_by(sku=sku).first()
                        if produto:
                            produto.custo = custo
                        else:
                            novo_produto = Produtos(sku=sku, custo=custo, quantidade_estoque=0)
                            session.add(novo_produto)

                    session.commit()
                    print("Tabela Produtos atualizada com sucesso!")
                except FileNotFoundError:
                    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
        else:
            print("Nenhum SKU sem custo foi encontrado, mas há SKUs não cadastrados.")


atualizar_custos()
