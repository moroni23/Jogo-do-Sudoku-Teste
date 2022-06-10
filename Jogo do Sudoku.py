
def ValidaLinha(sudoku, valor, indexLinha):
    for indexColuna in range(len(sudoku[indexLinha])):
        if (sudoku[indexLinha][indexColuna] == valor):
            return False
    return True

def ValidaColuna(sudoku, valor, indexColuna):
    #Está incorreto!!!
    #Você deverá iterar entre as linhas da coluna escolhida e validar se a [linha][coluna]
    # possui o valor escolhido. Caso possue, retorne False. Se o looping terminar, retorne True.
    #Dica: o numero de linhas você deverá pegar assim - len(sudoku)

    for indexlinha in range(len(sudoku[indexColuna])):
        if (sudoku[indexColuna[indexlinha == valor]]):
            return False
    return True

def ValidaQuadrante(sudoku, valor, indexLinha, indexColuna):
    for valor_linha in range(dividelinha* 3):
        for valor_linha in range(dividelinha * 3 + 3):
            if valor_linha == dividelinha:
                return False
            else:
                return True
    for valor_coluna in range(dividecoluna *3):
        for valor_coluna in range(dividecoluna * 3 + 3):
            if valor_coluna == dividecoluna:
                return False
            else:
                return True

    #Está incorreto!!!
    #Você precisa armazenar em duas variáveis, os valores da divisão truncada por 3 da linha e coluna, respectivamente.
    #Você então irá fazer uma iteração encadeada (um for dentro de outro for).
    #   Na primeira iteração vc considerará como range:
    #       1 - valor da divisão truncada por 3 da linha, multiplicado por 3
    #       2 - valor da divisão truncada por 3 da linha, multiplicado por 3, e isso somado de 3
    #       Ex: range(qtdQuadrantesLinha * 3,qtdQuadrantesLinha * 3 +3)
    #   Na segunda iteração vc considerará como range:
    #       1 - valor da divisão truncada por 3 da coluna, multiplicado por 3
    #       2 - valor da divisão truncada por 3 da coluna, multiplicado por 3, e isso somado de 3
    #       Ex: range(qtdQuadrantesColuna * 3,qtdQuadrantesColuna * 3 +3)
    #Dentro dessa iteração encadeada, você irá colocar uma condição, se a linha e coluna correspondentes a iteração atual possuem
    # o valor escolhido, retorne False. Se a iteração encadeada terminar, retorne True.

valor_linha = int(input('Digite um número de 1 a 9: '))
valor_coluna = int(input('Digite um número de 1 a 9: '))
dividelinha = valor_linha // 3
dividecoluna = valor_coluna //3

def PrintarSudoku(board):
        print("-" * 37)#Explicação:
        for i, row in enumerate(board):#Explicação:
            print(("|" + " {}   {}   {} |"*3)#Explicação:
                  .format(*[x if x != 0 else " " for x in row]))#Explicação:
            if i == 8:#Explicação:
                print("-" * 37)
            elif i % 3 == 2:#Explicação:
                print("|" + "---+" * 8 + "---|")
            else:#Explicação:
                print("|" + "   +" * 8 + "   |")

sudoku = [
     [0, 0, 2, 3, 0, 2, 0, 6, 0],
     [9, 0, 0, 3, 0, 5, 0, 0, 1],
     [0, 0, 1, 8, 0, 6, 4, 0, 0],
     [0, 0, 8, 1, 0, 2, 9, 0, 0],
     [7, 0, 0, 0, 0, 0, 0, 0, 8],
     [0, 0, 6, 7, 0, 8, 2, 0, 0],
     [0, 0, 2, 6, 0, 9, 5, 0, 0],
     [8, 0, 0, 2, 0, 3, 0, 0, 9],
     [0, 0, 5, 0, 1, 0, 3, 0, 0]
    ]






