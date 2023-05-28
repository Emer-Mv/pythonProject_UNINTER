nome = 'Emerson'
ru = 4191452
print(f'Bem vindo a loja do {nome}\nRU:{ru}')
val = float(input('Valor do Produto: '))
Qtd = int(input('Quantidade de Produtos: '))
subtotal = val * Qtd
total = 0
if Qtd <= 9:
    total += subtotal
elif 10 >= Qtd <= 99:
    print('Você ganhou 5% de desconto!\n')
    total += subtotal - subtotal * 0.05

elif 100 >= Qtd <= 999:
    print('Você ganhou 10% de desconto!\n')
    total += subtotal - subtotal * 0.10
else:
    print('Você ganhou 15% de desconto!\n')
    total += subtotal - subtotal * 0.15
desconto = subtotal - total
print(f'Total sem Desconto:R$ {subtotal:.2f}')
print(f'Desconto Concedido:R$ {desconto:.2f}')
print(f'Total com Desconto:R$ {total:.2f}')


#print(f'Total sem Desconto:R$  {subtotal:.2f}\nDesconto Concedido:R$  {desconto:.2f}\nTotal com Desconto:R$ {total:.2f}')