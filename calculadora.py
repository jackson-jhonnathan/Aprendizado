#QUESTIONAMENTO AO USUARIO
print('Olá, Seja Bem-Vindo a minha calculadora!')
print()
while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Escolha uma opção de operador: (+-/*) ')

#PROCESSAMENTO DO CODÍGO

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Um ou ambos dos operadores digitados são inválidos.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    if operador == '+':
     print(num_1_float + num_2_float)    
    elif operador == '-':
     print(num_1_float - num_2_float) 
    elif operador == '/':
     print(num_1_float / num_2_float)
    elif operador == '*':
     print(num_1_float * num_2_float)
#FINALIZAÇÃO DO CODÍGO    
    sair = input('Deseja sair? [S] and [N] ')
    sair = sair.lower() # .lower retorna qualquer string escrita em maisculo para minusculo.
    sair = sair.startswith('s') # .startswith verifica se a palavra começa com a inicial setada por você, no caso 's' nesse exemplo.
    if sair is True:
        break # caso a condição acima seja verdadeira, o comando BREAK vai encerrar a condição.
