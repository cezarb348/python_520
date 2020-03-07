# -*- coding: utf-8 -*-

# n = 1

# while n < 10:
#     print(f'Numero: {n}')
#     n += 1

# print('fim do while! ')

# frutas = ['limao','pera','abacaxi','maca','uva']

# for fruta in frutas:
#     print(fruta)

# cont = 0

# while cont < 10:
#     print(f'vezes de execucao {cont + 1}')
#     if cont == 5:
#         print('bloco de condicao que que interrompe o loop')
#         break
#     cont += 1

# impar = []

# for num in range(20):
#     if num % 2 == 0:
#         continue
#     else:
#         impar.append(num)

# print(impar)


usuarios = ['maria','joao','caio','roberto']

#controle de loop com while
while True:

    usuario = input('Digite seu login: ') 

    if usuario.lower() in usuarios: 
        print('Acesso concedido')
        break
    else: 
        print('Acesso negado')
        continue