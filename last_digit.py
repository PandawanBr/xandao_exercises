#!/usr/bin/python3

# Given a number (greater or equal to zero), write a program which returns the last digit of the number.

def lastDigit(number):
    length = len(number) - 1
    return int(number[length:])

number = str(input("Insira um numero inteiro: "))
print('Ultimo Digito: ', lastDigit(number))
