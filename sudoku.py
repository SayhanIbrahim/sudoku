
import numpy as np
import random

# boardcalcul = [["0" for x in range(9)] for y in range(9)]
sudokuboard = list()
dic_rc99 = dict()
dic_rc99control = ()


class CreateBoard:
    def openfileCreateSboard():
        global sudokuboard
        fichier = open('sudoku1.txt', 'r')
        for line in fichier:
            linelist = []
            for chiffre in line:
                if chiffre != "\n":
                    if chiffre == "_":
                        chiffre = 0
                    linelist.append(int(chiffre))
            sudokuboard.append(linelist)
        fichier.close()
        return sudokuboard

    def dictcreater():
        global sudokuboard
        dic_rc99 = {(rx, cx): c for rx, r in enumerate(sudokuboard)
                    for cx, c in enumerate(r)}
        for key in dic_rc99:
            if dic_rc99[key] == 0:
                dic_rc99[key] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                continue

        return dic_rc99

    def regioncreate():
        global sudokuboard  # for create a matrix with regions of sudoku
        r00 = []
        r01 = []
        r02 = []
        r10 = []
        r11 = []
        r12 = []
        r20 = []
        r21 = []
        r22 = []
        regionlist = [[r00, r01, r02], [r10, r11, r12], [r20, r21, r22]]
        for row in range(9):
            for col in range(9):
                # for append all elemenets of sudoku to the matrix of sudoku regions
                rowlist = sudokuboard[row]
                element = rowlist[col]
                rowi = row//3
                coli = col//3
                if rowi == 0 and coli == 0:
                    r00.append(element)
                elif rowi == 0 and coli == 1:
                    r01.append(element)
                elif rowi == 0 and coli == 2:
                    r02.append(element)
                elif rowi == 1 and coli == 0:
                    r10.append(element)
                elif rowi == 1 and coli == 1:
                    r11.append(element)
                elif rowi == 1 and coli == 2:
                    r12.append(element)
                elif rowi == 2 and coli == 0:
                    r20.append(element)
                elif rowi == 2 and coli == 1:
                    r21.append(element)
                elif rowi == 2 and coli == 2:
                    r22.append(element)
                else:
                    continue
        return regionlist


def zerocounter(sudokuboard):
    # for count all of the zeros in the sudokuboard
    cnt = 0
    for row in sudokuboard:
        for chiffre in row:
            if chiffre == 0:
                cnt = cnt+1
    # for calculate how many for loops in the research function
    cnt = (cnt//9)+1
    print(cnt)
    return cnt


def researchMatrix0s():
    global sudokuboard
    sudokuboard = CreateBoard.openfileCreateSboard()
    dic_rc99 = CreateBoard.dictcreater()
    cnt = zerocounter(sudokuboard)
    print(cnt)
    for i in range(25):
        for (row, col) in dic_rc99:
            if sudokuboard[row][col] == 0:
                rowi = row//3
                coli = col//3
                liste = dic_rc99[(row, col)]
                for i in range(3):
                    # i dont know why but it works with 3, maybe because of 3*3=9 region or 3 tip control: row, colomn, region :-)
                    # I converted the sudoku board to array because of its easy to control each row and column with numpy
                    sudokuboardarr = np.array(sudokuboard)
                    sudokuboardTarr = np.transpose(sudokuboardarr)
                    regionlist = CreateBoard.regioncreate()
                    # Maybe i dont need it, but i`m ametor i will learn how can i do with numpy arrays
                    sudokuboardrowlist = sudokuboardarr[row].tolist()
                    sudokuboardTcolumlist = sudokuboardTarr[col].tolist()
                    for chiffre in liste:
                        if chiffre in sudokuboardrowlist:
                            liste.remove(chiffre)
                    for chiffre in liste:
                        if chiffre in sudokuboardTcolumlist:
                            liste.remove(chiffre)
                    for chiffre in liste:
                        if chiffre in regionlist[rowi][coli]:
                            liste.remove(chiffre)
                    if len(liste) == 1:
                        dic_rc99[(row, col)] = liste[0]
                        sudokuboard[row][col] = liste[0]

    # sudokuboardControl = openfileCreateSboard()
    for line in sudokuboard:
        print(line)
    # cnt = zerocounter(sudokuboard)
    # print(cnt)
    # sudokuboardControl = sudokuboard
    # probabiltylst = []
    # probabilty = []
    # while True:
    #     def randomsudoku():
    #         for (row, col) in dic_rc99:
    #             if type(dic_rc99[(row, col)]) is int:
    #                 continue
    #             else:
    #                 p = random.choice(dic_rc99[(row, col)])
    #                 sudokuboardControl[row][col] = p
    #                 probabilty.append(''.join(p))

    #     if probabilty[0] in probabiltylst:
    #         randomsudoku()
    #     else:
    #         probabiltylst.append(probabilty)

    #     sudokuboardarr = np.array(sudokuboardControl)
    #     sudokuboardTarr = np.transpose(sudokuboardarr)
    #     regionlist = CreateBoard.regioncreate()
    #     liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #     def searchmistake():
    #         for i in range(len(liste)):
    #             counter = 0
    #             # i dont know why but it works with 3, maybe because of 3*3=9 region or 3 tip control: row, colomn, region :-)
    #             # I converted the sudoku board to array because of its easy to control each row and column with numpy
    #             sudokuboardarr = np.array(sudokuboardControl)
    #             sudokuboardTarr = np.transpose(sudokuboardarr)
    #             # regionlist = CreateBoard.regioncreate()
    #             # Maybe i dont need it, but i`m ametor i will learn how can i do with numpy arrays
    #             sudokuboardrowlist = sudokuboardarr[i].tolist()
    #             # sudokuboardTcolumlist = sudokuboardTarr[col].tolist()
    #             for chiffre in liste:
    #                 if sudokuboardrowlist.count(chiffre) > 0:
    #                     print(chiffre, sudokuboardarr[i],
    #                           sudokuboardrowlist.count(chiffre))
    #                     randomsudoku()
    #                 else:
    #                     continue
    #             for chiffre in liste:
    #                 if sudokuboardTarr.count(chiffre) > 0:
    #                     print(chiffre, sudokuboardTarr[i],
    #                           sudokuboardTarr.count(chiffre))
    #                     randomsudoku()
    #                 else:
    #                     continue

        # searchmistake()
        # for chiffre in liste:
        #     if chiffre in sudokuboardTcolumlist:
        #         liste.remove(chiffre)
        # for chiffre in liste:
        #     if chiffre in regionlist[rowi][coli]:
        #         liste.remove(chiffre)
        # if len(liste) == 1:
        #     dic_rc99[(row, col)] = liste[0]
        #     sudokuboard[row][col] = liste[0]

    for (row, col) in dic_rc99:
        print((row, col), dic_rc99[(row, col)])


researchMatrix0s()
