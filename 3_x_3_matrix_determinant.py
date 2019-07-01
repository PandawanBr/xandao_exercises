#!/usr/bin/python3
# link onde foi visto como fazer a determinante: https://brasilescola.uol.com.br/matematica/determinantes-1.htm
# Write a program which calculates the determinant of a 3 x 3 matrix.
matrix = [[2, 5, 6], [1, 6, 7], [-1, 2, 3]]

def matrixDeterminant(array):
    diagonalPrincipal = [1, 1, 1]
    diagonalSecundaria = [1, 1, 1]
    for x in range(len(array[0])):
        diagonalPrincipal[0] *= array[x][x]
        diagonalSecundaria[0] *= array[x][(len(array[0]) - 1) - x]

        if x == 0:
            diagonalPrincipal[1] *= array[x][x + 1]
            diagonalPrincipal[2] *= array[x][x + 2]
            diagonalSecundaria[1] *= array[x + 2][x + 1]
            diagonalSecundaria[2] *= array[x + 2][x + 2]
        elif x == 1:
            diagonalPrincipal[1] *= array[x][x + 1]
            diagonalPrincipal[2] *= array[x][x - 1]
            diagonalSecundaria[1] *= array[x][x + 1]
            diagonalSecundaria[2] *= array[x][x - 1]
        else:
            diagonalPrincipal[1] *= array[x][x - 2]
            diagonalPrincipal[2] *= array[x][x - 1]
            diagonalSecundaria[1] *= array[x - x][x - x]
            diagonalSecundaria[2] *= array[x - 2][x - 1]
    return (sum(diagonalPrincipal) - sum(diagonalSecundaria))

print('Determinante da Matriz', matrixDeterminant(matrix))
