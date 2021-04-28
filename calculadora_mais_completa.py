
while True:
    print()
    num_1 = input('Digite um nº: ')
    num_2 = input('Digite outro nº: ')
    operador = input('Digite um operador: ')

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(f' O resultado da conta é: {num_1 + num_2}')
        sair = input('Deseja sair? digite: [s] para sim ou [n] para não: ')
        if sair == 's':
            break

    elif operador == '-':
        print(f' O resultado da conta é: {num_1 - num_2}')
        sair = input('Deseja sair? digite: [s] para sim ou [n] para não: ')
        if sair == 's':
            break

    elif operador == '/':
        print(f' O resultado da conta é: {num_1 / num_2}')
        sair = input('Deseja sair? digite: [s] para sim ou [n] para não: ')
        if sair == 's':
            break

    elif operador == '*':
        print(f' O resultado da conta é: {num_1 * num_2}')
        sair = input('Deseja sair? digite: [s] para sim ou [n] para não: ')
        if sair == 's':
            break

