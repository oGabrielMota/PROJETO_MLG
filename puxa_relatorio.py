import pandas as pd
import re
from banco_dados import Conta, Conteudo_Relatorio, Relatorio, Produtos, session
from cria_conta import cria_contas
from subindo_skus import subindo_novos_skus



contas_criadas = session.query(Conta).all()

if len(contas_criadas) == 0:
    cria_contas()


#Itens que seram dinamicos depois
id_conta = int(input('Para qual conta é esse relatorio?'))
nome_arquivo = "teste01.xlsx"

conta_existente = session.query(Conta).filter_by(id=id_conta).first()

dados_relatorio = pd.read_excel(nome_arquivo, skiprows=6,
                                usecols=[1,2,6,7,14,17,18]
                                )
puxa_data = pd.read_excel(nome_arquivo).iloc[2,0]
data_relatorio = re.sub(r'^Vendas  Status das suas vendas em |, às .*$', '', puxa_data)

##Codigo que segue

array_resultado = dados_relatorio.values.tolist()
skus_sem_custo = []


for resultados in array_resultado:
    sku_atual = resultados[5] 
    lucro_bruto = resultados[4]
    unidades = resultados[2] 

    # Buscar o produto pelo SKU na tabela Produtos
    produto = session.query(Produtos).filter_by(sku=sku_atual).first()
    

    if produto and produto.custo > 0:
        custo_total = produto.custo * unidades
        lucro_liquido = lucro_bruto - custo_total
    else:
        lucro_liquido = 0.0
        skus_sem_custo.append(sku_atual)

    novo_item = Conteudo_Relatorio(
        status=resultados[1],
        data=resultados[0],
        unidade=unidades,
        valor_venda=resultados[3],
        lucro_bruto=lucro_bruto,
        lucro_liquido=lucro_liquido,
        sku=sku_atual,
        mlb=re.sub(r'\D', '', str(resultados[6]))
    )
    session.add(novo_item)


if skus_sem_custo:
    skus_sem_custo = list(set(skus_sem_custo))  # Remover duplicados
    print(f"\nAtenção! Encontramos {len(skus_sem_custo)} SKU(s) sem custo.")
    resposta = input("Deseja gerar uma planilha para adicionar os custos? (s/n): ")
    if resposta.lower() == "s":
        df_custos = pd.DataFrame(skus_sem_custo, columns=['SKU'])
        df_custos['custo'] = 0.0
        df_custos.to_excel("skus_sem_custo.xlsx", index=False)
        print("Arquivo 'skus_sem_custo.xlsx' criado com sucesso!")
    
    subindo_novos_skus()


if conta_existente:
    novo_relatorio = Relatorio(
    conta= id_conta,
    lucro_dia= 0,
    data= data_relatorio
)
    session.add(novo_relatorio)
    print(f"Relatório inserido com sucesso!")
else:
 print(f"Conta com id {id_conta} não encontrada!")


session.commit()
print("Dados inseridos com sucesso via array_resultado!")
