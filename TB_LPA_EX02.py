nome = 'Emerson Vaz'
ru = 4191452
print(f'Bem vindo a lanchonete do {nome}\nRU:{ru}\n')
print('*' * 17, 'Menu', '*' * 16)
print('|Código|       Descrição        |Valor|')
print('|  100 |    Cachorro-Quente     |9.00 |')
print('|  101 | Cachorro-Quente Duplo  |11.00|')
print('|  102 |       X-Egg            |12.00|')
print('|  103 |      X-Salada          |13.00|')
print('|  104 |       X-Bacon          |14.00|')
print('|  105 |       X-Tudo           |17.00|')
print('|  200 |    Refrigerante Lata   |5.00 |')
print('|  201 |      Chá Gelado        |4.00 |')
print('-'*39)
total = 0

while True:
    codigo = int(input('Digite o codigo do pedido!'))
    if codigo == 100:
        total += 9.00
        print('Você pediu um Cachorro-Quente no valor de:R$9.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Valor inválido, por favor digite um valor válido!')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 101:
        total += 11.00
        print('Você pediu um Cachorro-Quente Duplo no valor de:R$11.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 102:
        total += 12.00
        print('Você pediu um X-Egg no valor de:R$12.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 103:
        total += 13.00
        print('Você pediu um X-Salada no valor de:R$13.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 104:
        total += 14.00
        print('Você pediu um X-Bacon no valor de:R$14.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 105:
        total += 17.00
        print('Você pediu um X-Tudo no valor de:R$17.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 200:
        total += 5.00
        print('Você pediu um Refrigerante Lata no valor de:R$5.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    elif codigo == 201:
        total += 4.00
        print('Você pediu um Chá Gelado no valor de:R$4.00')
        print(f'Total a ser pago é: R${total:.2f}')
        pedir_m1 = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - nao\n'))

        if pedir_m1 == 1:
            continue
        elif pedir_m1 == 0:
            print(f'Obrigado e volte Sempre\nTotal a ser pago é: R${total:.2f}')
            break

        while pedir_m1 != 1:
            print('Opção inválida, por favor digite uma opção válida')
            pedir_m1 = int(input('Deseja fazer mais um pedido?\n1 - sim\n0 - Não\n'))

            continue

    else:
        print('Opção inválida, por favor digite uma opção válida')
        continue