from random import randint

print('VOCÊ CONSEGUE ADVINHAR O MESMO NÚMERO QUE EU?')

computador = randint(1, 6)
jogador = int(input('Digite um número de 1 a 5: '))

if jogador >= 6:

  print('Digite um número de 1 a 5!')
  
elif jogador == computador:

  print(f'Você escolheu o  número {jogador} e o computador escolheu o número {computador}')
  
  print('Parabens você acertou!')
  
else:

  print(f'Você escolheu o  número {jogador} e o computador escolheu o número {computador}')
  
  print('ERROU!!!')
