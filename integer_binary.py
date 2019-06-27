#!/usr/bin/python3

number = int(input("Digite um numero inteiro: "))
binary = 0
mult = 1
while(0 < number):
    binary += int((number % 2) * mult)
    number = int(number / 2)
    mult *= 10
else:
    print("binario: {}".format(binary))
