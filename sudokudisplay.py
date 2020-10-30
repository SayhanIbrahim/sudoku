import pygame
import sys
from pygame.locals import QUIT
from sudokuversion2 import openfilecreatesboard, solve
import os


height = 603
width = 603
color = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((width, height+100))
pygame.display.set_caption('Sudoku Solver')
FPS = 60
FramePerSec = pygame.time.Clock()
background = pygame.Surface(screen.get_size())


def startscreen():
    global background
    pygame.init()
    screen = pygame.display.set_mode((width, height+100))
    background = background.convert()
    background.fill(white)
    # Display button text
    font = pygame.font.Font(None, 36)
    text1 = font.render("Load Sudoku", 1, black)
    text2 = font.render("Solve Sudoku", 1, black)
    text3 = font.render("Reset", 1, black)
    textpos1 = text1.get_rect(center=(100, 650))
    textpos2 = text1.get_rect(center=(300, 650))
    textpos3 = text1.get_rect(center=(520, 650))
    background.blit(text1, textpos1)
    background.blit(text2, textpos2)
    background.blit(text3, textpos3)

    # drawing vertical lines
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(background, black, (i*width/9, 0),
                             (i*width/9, height+100), 7)
        else:
            pygame.draw.line(background, black, (i*width/9, 0),
                             (i*width/9, height), 4)
    # drawing horizontal lines
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(background, black,
                             (0, i*width/9), (603, i*width/9), 7)
        else:
            pygame.draw.line(background, black,
                             (0, i*width/9), (603, i*width/9), 4)
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.update()
    pygame.display.flip()


def nextcell(row=0, col=0):
    nextcol = col+1
    if nextcol == 9:
        nextrow = row+1
        nextcol = 0
    else:
        nextrow = row
    return (nextrow, nextcol)


def loadsudoku():  # Blit everything in the given sudoku to the screen
    board = openfilecreatesboard()
    solve(board)
    font = pygame.font.Font(None, 30)
    row, col = 0, 0
    for line in board:
        for element in line:
            if element == 0:
                row, col = nextcell(row, col)
                continue
            else:
                message = str(element)
                text = font.render(message, 2, black)
                textpos = text.get_rect(center=(33+col*67, 33+row*67))
                row, col = nextcell(row, col)
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
                pygame.display.update()


def solvesudoku():  # Blit everything in the solution of sudoku to the screen
    boardsolution = openfilecreatesboard("solution.txt")
    boardcontrol = openfilecreatesboard()
    row, col = 0, 0
    font = pygame.font.Font(None, 30)
    for line in boardcontrol:
        for element in line:
            if element == 0:
                message = boardsolution[row][col]
                message = str(message)
                text = font.render(message, 2, color)
                textpos = text.get_rect(center=(33+col*67, 33+row*67))
                row, col = nextcell(row, col)
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
                pygame.display.update()
            else:
                row, col = nextcell(row, col)
                continue


def gamereset():  # For reset game
    os.remove("solution.txt")
    pygame.init()
    startscreen()


def mouseclick():
    x, y = pygame.mouse.get_pos()
    if x < 200 and y > 600:
        loadsudoku()
    elif 200 < x < 400 and y > 600:
        solvesudoku()
    elif 400 < x < 600 and y > 600:
        gamereset()
    else:
        pass


startscreen()
# Event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            try:
                os.remove("solution.txt")
                pygame.quit()
                sys.exit()
            except:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclick()

    pygame.display.update()
    FramePerSec.tick(FPS)
