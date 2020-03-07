# -*- coding: utf-8 -*-


# while True:
#     try:
#         x = int(input('Digite o primeiro numero: '))
#         y = int(input('Digite o segundo numero: '))
#         print(f'Resultado: {x / y}')
#         break
#     except ValueError as t:
#         print(t)
#         print('Digite apenas numeros!')
#         continue
#     except ZeroDivisionError as z:
#         print(z)
#         print('Numero dividido por zero')
#         continue
#     finally:
#         print('Calculo de divisao')

#raise exception

funcionarios = ['rafael','mariana','paulo']


try:
    f = input('Nome: ')
    if f in funcionarios:
        print('voce e um funcionario')
    else:
        raise NameError('Voce nao e funcionario')

except NameError as n:
    print(n)