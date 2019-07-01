#!/usr/bin/python3
import random

print("Gerador de Xablau")
number = int(input("Insira o numero de palavras a aparecer: "))
randomList = []
stringMessage = ''
xablau_frases = ['quêêêêêê', 'perc', 'fiforn', 'tipoType', 'énada', 'percAss',
                 'vouBotarNaSuaBranch', 'tranquera', 'canalha', 'xablau', 'gcp',
                 'putz', 'chorando', 'valValor', 'trocaBem', 'caaaraaamba', 'taCerto',
                 'QuatroEvinte', 'naoSePodeGanharTodas', 'aceiteMinhaDerrotaPoisEuJaAceitei']

for x in range(number):
    randomList.append(xablau_frases[random.randint(0, (len(xablau_frases)-1))])

if len(randomList) > 0:
    for x in range(len(randomList)):
        if stringMessage != '':
            stringMessage += '; {}'.format(randomList[x])
        else:
            stringMessage += randomList[x]
    print(stringMessage)
else:
    print("Nenhum item selecionado")

