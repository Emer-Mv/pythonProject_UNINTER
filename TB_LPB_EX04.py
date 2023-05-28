print('Bem Vindo ao Controle de Peças')

peca = []

def cadastrarPeca(codigo):
    print('Cadastrar Peça: ')

    print(f'Codigo da Peça {codigo}')

    nome = input('Digite o Nome da Peça:')

    fabricante = input('Digite o Fabricante da Peça:')

    valor = float(input('Valor da peça: '))

    cadastroEstoque = {'Codigo':     codigo,
                          'Nome':       nome,
                          'Fabricante': fabricante,
                          'Valor':      valor}

    peca.append(cadastroEstoque.copy())

    cadastroEstoque.clear()

def consultarPeca():
    while True:
        print('Consultar Peça')
        opConsulta = int(input(
            'Escolha a Opção Desejada:\n1 - Consultar Todas as pecas\n2 - Por Codigo\n3 - Por Fabricante\n4 - Retornar '))

        if opConsulta == 1:
            print('-' * 11)
            for registro in peca:
                for key, value in registro.items():
                    print(f'{key} : {value}')

                    print('-' * 11)

        elif opConsulta == 2:
            entrada = int(input('Digite o Codigo da Peça: '))
            print('-' * 11)
            for registro in peca:
                if registro['codigo'] == entrada:
                    for key, value in registro.items():
                        print(f'{key} : {value}')

                        print('-' * 11)

        elif opConsulta == 3:
            entrada = input('Digite o Fabricante: ')

            print('-' * 11)

            for registro in peca:
                if registro['fabricante'] == entrada:
                    for key, value in registro.items():
                        print(f'{key} : {value}')

                        print('-' * 11)
            else:
                opConsulta == 4
                continue


def removerPeca():
    print('Remover Peça: ')
    entrada = input('Codigo Para Remoção: ')


for registro in peca:
    if registro['codigo'] == entrada:
        peca.remove(registro)



registroPeca = 0

while True:
    opcao = int(input('1 - Cadastrar\n2 - Consultar\n3 - Remover\n4 - Sair\n\n'))
    if opcao == 1:
        registroPeca += 1
        cadastrarPeca(registroPeca)

    elif opcao == 2:
        consultarPeca()
    elif opcao == 3:
        removerPeca()

    else:
        print('Sair')

        break




