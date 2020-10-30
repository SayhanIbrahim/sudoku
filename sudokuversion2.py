import numpy as np
import copy


def openfilecreatesboard(filename='sudoku.txt'):
    fichier = open(filename, 'r')
    board = []
    for line in fichier:
        linelist = []
        for chiffre in line:
            if chiffre != "\n":
                if chiffre == "_":
                    chiffre = 0
                linelist.append(int(chiffre))
        board.append(linelist)
    fichier.close()
    # sudokuprinter(board)
    return board


def sudokuprinter(board):
    for line in board:
        print(line)


def rowlist(board, row):
    return board[row]


def columnlist(board, col):
    sudokuboardarr = np.array(board)
    sudokuboardTarr = np.transpose(sudokuboardarr)
    columlist = sudokuboardTarr[col].tolist()
    return columlist


def regionlist(board, row, col):
    regionlist = []
    rowi = row//3
    coli = col//3
    for i in range(3):
        for j in range(3):
            regionlist.append(board[3*rowi+i][3*coli+j])
    return regionlist


def checkcell(board, cell, row, col):
    if cell in rowlist(board, row):
        return False
    elif cell in columnlist(board, col):
        return False
    elif cell in regionlist(board, row, col):
        return False
    else:
        return True


def solve(controlboard, row=0, col=0):
    board = copy.deepcopy(controlboard)
    nextcol = col+1
    if nextcol == 9:
        nextrow = row+1
        nextcol = 0
    else:
        nextrow = row
    if board[row][col] == 0:
        numlist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        while True:
            if len(numlist) == 0:
                return
            cell = numlist.pop()
            if checkcell(board, cell, row, col):
                board[row][col] = cell
                if row == 8 and col == 8:
                    print("Sudoku Solved by AI")
                    # sudokuprinter(board)
                    stringconverter(board)
                else:
                    solve(board, nextrow, nextcol)
    else:
        solve(board, nextrow, nextcol)

    return board


def stringconverter(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            board[i][j] = str(num)
    solutioncollecter(board)


def solutioncollecter(board):
    solutionlist = []
    for i in range(9):
        line = "".join(board[i])
        solutionlist.append(line)
    solutionwrite(solutionlist)
    return


def solutionwrite(solutionlist):
    for i in range(9):
        line = str(solutionlist[i])
        ths = open("solution.txt", "a")
        ths.write(line+"\n")
        ths.close()


board = openfilecreatesboard()
solve(board)
