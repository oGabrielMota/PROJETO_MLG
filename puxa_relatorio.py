import pandas as pd
import re
from banco_dados import Conta, Conteudo_Relatorio, Relatorio, session
import cria_conta


cria_conta

#Itens que seram dinamicos depoiss
id_conta = 1 #Corresponde conta Aron
nome_arquivo = "teste01.xlsx"

conta_existente = session.query(Conta).filter_by(id=id_conta).first()

dados_relatorio = pd.read_excel(nome_arquivo, skiprows=6,
                                usecols=[1,2,6,7,14,17,18]
                                )
puxa_data = pd.read_excel(nome_arquivo).iloc[2,0]
data_relatorio = re.sub(r'^Vendas  Status das suas vendas em |, às .*$', '', puxa_data)

##Codigo que segue

array_resultado = dados_relatorio.values.tolist()


for resultados in array_resultado:
    novo_item = Conteudo_Relatorio(
        status=resultados[1],
        data=resultados[0],
        unidade=resultados[2],
        valor_venda=resultados[3],
        lucro_bruto=resultados[4],
        sku=resultados[5],
        mlb=re.sub(r'\D', '', str(resultados[6]))
    )
    session.add(novo_item)


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
