from banco_dados import Conta, session

meta_conta_antiga = 120000
meta_conta_nova = 80000
valor_vendido = 0

def cria_contas():

    aron = Conta(
        meta= meta_conta_antiga,
        nome_conta= 'Aron',
        valor_restante= meta_conta_antiga - valor_vendido,
        valor_vendido=0
    )

    aline = Conta(
        meta= meta_conta_antiga,
        nome_conta= 'Aline',
        valor_restante= meta_conta_antiga - valor_vendido,
        valor_vendido=0
    )

    alex = Conta(
        meta= meta_conta_antiga,
        nome_conta= 'Alex',
        valor_restante= meta_conta_antiga - valor_vendido,
        valor_vendido=0
    )

    beth = Conta(
        meta= meta_conta_antiga,
        nome_conta= 'Beth',
        valor_restante= meta_conta_antiga - valor_vendido,
        valor_vendido=0
    )

    geralda = Conta(
        meta= meta_conta_antiga,
        nome_conta= 'Geralda',
        valor_restante= meta_conta_antiga - valor_vendido,
        valor_vendido=0
    )

    guilherme = Conta(
        meta= meta_conta_nova,
        nome_conta= 'Guilherme',
        valor_restante= meta_conta_nova - valor_vendido,
        valor_vendido=0
    )

    higrer = Conta(
        meta= meta_conta_antiga,
        nome_conta= 'Higrer',
        valor_restante= meta_conta_antiga - valor_vendido,
        valor_vendido=0
    )

    zhs = Conta(
        meta= meta_conta_nova,
        nome_conta= 'ZHS',
        valor_restante= meta_conta_nova - valor_vendido,
        valor_vendido=0
    )

    sergio = Conta(
        meta= meta_conta_nova,
        nome_conta= 'Sergio',
        valor_restante= meta_conta_nova - valor_vendido,
        valor_vendido=0
    )


    session.add(aron)
    session.add(aline)
    session.add(alex)
    session.add(beth)
    session.add(geralda)
    session.add(guilherme)
    session.add(higrer)
    session.add(zhs)
    session.add(sergio)

    session.commit()
    print("Contas adicionada com sucesso!")
