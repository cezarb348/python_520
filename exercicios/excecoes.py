# dada a lista

funcionarios = ['joao','maria','carlos','paula','mario','frodo']

while True:

    try:
        usuario = input('Digite seu usuario: ') 
        if usuario in funcionarios:
            if usuario == 'frodo':
                raise NameError('Usuario desligado, passar no RH')
            else:
                print('Acesso permitido')
                break
        else:
            print('Acesso negado')
            continue
    except NameError as negado:
            print(negado)