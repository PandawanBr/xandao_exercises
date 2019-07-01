#!/usr/bin/python3

# Write a program which converts a number (greater or equal to zero) into its binary representation.

number = int(input("Digite um numero inteiro: "))
binary = 0
mult = 1
while(0 < number):
    binary += int((number % 2) * mult)
    number = int(number / 2)
    mult *= 10
else:
    print("binario: {}".format(binary))
