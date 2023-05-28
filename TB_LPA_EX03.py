
nome = 'Emerson Vaz'
ru = 4181452
print(f'Bem vindo a FastLog empresa de logística fundada por {nome}\ne que já realizou mais de {ru} entregas em todo sudeste!\n')

def dimensoesObjetos():

  while True:
    try:
        altura = float(input('Digite a altura do objeto (em cm): '))
        comprimento = float(input('Digite o comprimento do objeto (em cm): '))
        largura = float(input('Digite a largura do objeto (em cm): '))

        volume = comprimento * largura * altura
        print(f'O volume do objeto é: {volume}')

        if volume <= 1000:
          return 10
        elif 1001 <= volume <=10000:
          return 20
        elif 10001 <= volume <=30000:
          return 30
        elif 30001 <= volume < 100000:
          return 50
        else:
          print('Não aceitamos objetos com dimensões tão grandes')
          print('Tente novamente')
          continue
    except ValueError:
        print('Valor não numérico')
        print('Tente novamente')
        continue


def pesoObjeto():

  while True:

    try:
      peso = float(input('Digite o peso do objeto em (Kg)\n'))

      if peso <= 0.1:
        return 1
      elif  0.11 <  peso <= 1:
        return 1.5
      elif 1.10 <= peso <= 10:
        return 2
      elif 10.1 <= peso <= 30:
        return 3
      else:
        print('nao aceito')
        continue
    except ValueError:
      print('valor nao numerico')
      print('tente novamente')
      continue

def rotaObjeto():

  print('RS - De Rio de Janeiro até São Paulo')
  print('SR - De São Paulo até Rio de Janeiro')
  print('BS - De Brasília até São Paulo')
  print('SB - De São Paulo até Brasília')
  print('BR - De Braília até Rio de Janeiro')
  print('RB - De Rio de Janeiro até Brasília\n')

  while True:
      rota = str(input('Selecione a rota :')).upper()

      if rota == 'RS':
        return 1
      elif rota == 'SR':
        return 1
      elif rota == 'BS':
        return 1.2
      elif rota == 'SB':
        return 1.2
      elif rota == 'BR':
        return 1.5
      elif rota == 'RB':
        return 1.5
      else:
        print('Rota inválida')
        print('Digite novamente')
        continue

Dimensoes = dimensoesObjetos()
Peso = pesoObjeto()
Rota = rotaObjeto()

total = Dimensoes * Peso * Rota
print(f'O valor total e : R${total:.2f}\nDimensoes: {Dimensoes:.2f} * Peso {Peso:.2f} * Rota: {Rota:.2f}')