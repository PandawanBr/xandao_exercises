#!/usr/bin/python3

def lastDigit(number):
    length = len(number) - 1
    return int(number[length:])

number = str(input("Insira um numero inteiro: "))
print('Ultimo Digito: ', lastDigit(number))
