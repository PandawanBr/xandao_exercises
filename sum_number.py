#!usr/bin/python3

# Write a program which calculates the sum of 1 to n numbers without using loops.

listSum = []
def arraySum(number):
    if number > 0:
        listSum.append(number)
        return arraySum(number - 1)
    elif len(listSum) > 0:
        return sum(listSum)
    else:
        return 0


number = int(input('Insira um numero inteiro: '))
print('Resultado da soma: {}'.format(arraySum(number)))