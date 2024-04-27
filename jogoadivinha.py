#Criei um pequeno script que faz a máquina jogar contra você, aonde ela "pensa" em um número e você tem que acerta o mesmo número que ela.


from random import randint
from time import sleep # importa uma função para contabilizar um time

computador = randint(0, 5) #Sortea uma número aleatorio
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
ad = int(input('Adivinhe o número que o computador está pensando de 0 a 5: '))
print('PROCESSANDO...')
sleep(2) #função para contabilizar um time
if ad == computador:
    print('Você pensou no mesmo número. Parabéns!!!')
else:
    print('Você é burro! Tente novamente.')
