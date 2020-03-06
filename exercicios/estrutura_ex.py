# dado a lista

# times = ['time', ['Corinthians', 'Palmeiras', 'São Paulo'], 'cores', ['Preto', 'Branco', 'Verde', 'Vermelho']]

# imprima na tela as seguintes mensagens:


# time: <nome_time>, cores: <cores_time> 

# print(f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][1]}')
# print(f'{times[0]}: {times[1][1]}, {times[2]}: {times[3][2]}, {times[3][1]}')
# print(f'{times[0]}: {times[1][2]}, {times[2]}: {times[3][0]}, {times[3][1]}, {times[3][3]}')

# dado o dicionario:

dados = {
    'estados': {
        'sp':{
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg':{
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }

}

# Imprima as seguintes informações:

# 1. Nome dos estados

# 2. Nome dos estados, quantidade de municipios e população

# print(f"Nome dos estados: {dados['estados']['sp']['nome']}, {dados['estados']['rj']['nome']}, {dados['estados']['mg']['nome']}")

# print(f"Nome dos estados: {dados['estados']['sp']['nome']}, {dados['estados']['rj']['nome']}, {dados['estados']['mg']['nome']}")
# print(f"Qtde municipios: {dados['estados']['sp']['municipios']}, {dados['estados']['rj']['municipios']}, {dados['estados']['mg']['municipios']}")
# print(f"Populacao: {dados['estados']['sp']['populacao']}, {dados['estados']['rj']['populacao']}, {dados['estados']['mg']['populacao']}")

# print(f"Nome: {dados['estados']['sp']['nome']}\nMunicipios: {dados['estados']['sp']['municipios']}\nPopulacao: {dados['estados']['sp']['populacao']}  ")

# Calculo de notas
# peça 4 notas do aluno
# se a nota final for maior que 7
# imprima aprovado
# se nao
# imprima reprovado

nota1 = int(input('Digite a sua primeira nota: '))
nota2 = int(input('Digite a sua segunda nota: '))
nota3 = int(input('Digite a sua terceira nota: '))
nota4 = int(input('Digite a sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 :
    print(f'Voce foi aprovado, sua media e {media}')
else:
    print(f'Voce foi reprovado, sua media e {media}')
