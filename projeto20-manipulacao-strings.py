#Estruture três códigos, os quais devem conter uma função de manipulação de string que obtenha resultado.

def contletras(palavra):
    numero = len(palavra)
    return numero

def maiuscula(palavra):
    caixaalta=palavra.upper()
    return caixaalta

def minuscula(palavra):
    caixabaixa=palavra.lower()
    return caixabaixa

#programa
palavra = str(input('Digite uma palavra: '))
print(f'A palavra digitada contém {contletras(palavra)} letras')
print(f'Todas as letras MAIÚSCULAS: {maiuscula(palavra)}')
print(f'Todas as letras minúsculas: {minuscula(palavra)}')
