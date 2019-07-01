#!/usr/bin/python3

word = str(input('Insira uma palavra pra saber se é palindromo: '))

if word == word[::-1]:
    print('É palindromo')
else:
    print('Não é palindromo')