#!/usr/bin/python3

# Write a program which returns true if a String is palindrome and false otherwise. 
# In this program you can use only the command to get a specific character in a String.

word = str(input('Insira uma palavra pra saber se é palindromo: '))

if word == word[::-1]:
    print('É palindromo')
else:
    print('Não é palindromo')