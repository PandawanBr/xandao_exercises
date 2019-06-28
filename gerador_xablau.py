#!/usr/bin/python3
import random

print("Gerador de Xablau")
number = int(input("Insira o numero de palavras a aparecer: "))

xablau_frases = ['quêêêêêê', 'perc', 'fiforn', 'tipoType', 'énada', 'percAss',
                 'vouBotarNaSuaBranch', 'tranquera', 'canalha', 'xablau', 'gcp',
                 'putz', 'chorando', 'valValor', 'trocaBem', 'caaaraaamba', 'taCerto',
                 'QuatroEvinte', 'naoSePodeGanharTodas', 'aceiteMinhaDerrotaPoisEuJaAceitei']

for x in range(number):
         print(xablau_frases[random.randint(0, (len(xablau_frases)-1))])

