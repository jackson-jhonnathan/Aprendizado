#0123456
#Jackson
print('Olá, Digite os dados solcitados.')
print()
nome = (input('Digite seu nome: '))
idade = (input('Digite sua idade: '))
print()
if nome == 'Jackson' and idade == '21': #Utilizado "and" para confirmar se as duas informações são verdadeiras.
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é', nome[::-1])
    print(f'Seu nome tem {len(nome)} letras') #"len" mostra a quantidade de caracteres dentro da variavel citada no código.
    print(f'A primeira letra do seu nome é {(nome[0])}')
    print(f'A ultima letra do seu nome é {(nome[6])}')
else:
    print('Você não digitou corretamente, tente novamente!')
