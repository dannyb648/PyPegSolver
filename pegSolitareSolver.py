# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 20:34:28 2014

@author: DannyB648
Version: 0.3

Purpose of this script is to play games of Peg Solitaire randomly until it successfully
completes the game. It will then print out the successful game moves to a .txt file.



STARTING PEG POSITION
   <---------x--------->
 ^ [2][2][1][1][1][2][2]
 | [2][2][1][1][1][2][2]
 | [1][1][1][1][1][1][1]
 y [1][1][1][0][1][1][1]
 | [1][1][1][1][1][1][1]
 | [2][2][1][1][1][2][2]
 v [2][2][1][1][1][2][2]


"""
import numpy
import sys

gameBoard = numpy.array(range(49)).reshape((7, 7))
moveList = numpy.array(range(132)).reshape((33,4))

x = 0 #X coord on board
y = 0 #Y coord on board
a = 0 #Interation on move list array
movePickedX = 0
movePickedY = 0
checkHorizontally = True
game = 0
textFile = "" 
# Key for gameBoard Array: 0 = Empty, 1 = Peg, 2 = Void.
def resetBoard(textFile):    
    textFile = open("game %d.txt" % game, "w")
    gameBoard[0][0] = 2
    gameBoard[0][1] = 2
    gameBoard[0][2] = 1
    gameBoard[0][3] = 1
    gameBoard[0][4] = 1
    gameBoard[0][5] = 2
    gameBoard[0][6] = 2
    gameBoard[1][0] = 2
    gameBoard[1][1] = 2
    gameBoard[1][2] = 1
    gameBoard[1][3] = 1
    gameBoard[1][4] = 1
    gameBoard[1][5] = 2
    gameBoard[1][6] = 2
    gameBoard[2][0] = 1
    gameBoard[2][1] = 1
    gameBoard[2][2] = 1
    gameBoard[2][3] = 1
    gameBoard[2][4] = 1
    gameBoard[2][5] = 1
    gameBoard[2][6] = 1
    gameBoard[3][0] = 1
    gameBoard[3][1] = 1
    gameBoard[3][2] = 1
    gameBoard[3][3] = 0
    gameBoard[3][4] = 1
    gameBoard[3][5] = 1
    gameBoard[3][6] = 1
    gameBoard[4][0] = 1
    gameBoard[4][1] = 1
    gameBoard[4][2] = 1
    gameBoard[4][3] = 1
    gameBoard[4][4] = 1
    gameBoard[4][5] = 1
    gameBoard[4][6] = 1
    gameBoard[5][0] = 2
    gameBoard[5][1] = 2
    gameBoard[5][2] = 1
    gameBoard[5][3] = 1
    gameBoard[5][4] = 1
    gameBoard[5][5] = 2
    gameBoard[5][6] = 2
    gameBoard[6][0] = 2
    gameBoard[6][1] = 2
    gameBoard[6][2] = 1
    gameBoard[6][3] = 1
    gameBoard[6][4] = 1
    gameBoard[6][5] = 2
    gameBoard[6][6] = 2
    return textFile #This returns textFile variable
    
def possibleMoves(x, y, a, checkHorizontally):
    x = 0
    y = 0
    checkHorizontally = True
    while x <= 6 and y <= 6:
        checkHorizontally = True
        if(x + 2 > 6):
            y = y + 1
        else:
            if(gameBoard[x][y] == 1 and gameBoard[x + 1][y] == 1 and gameBoard[x + 2][y] == 0):
                saveMoveLeft()
                x = x + 1
            elif(gameBoard[x][y] == 0 and gameBoard[x + 1][y] == 1 and gameBoard[x + 2][y] == 1):
                saveMoveRight()
                x = x + 1
            else:
                x = x + 1
    while(x <= 6 and y <= 6):
        checkHorizontally = False
        if(y + 2 > 6):
            x = x + 1
        else:
            if(gameBoard[x][y] == 1 and gameBoard[x][y + 1] == 1 and gameBoard[x][y + 2] == 0):
                saveMoveDown()
                y = y + 1
            elif(gameBoard[x][y] == 0 and gameBoard[x][y + 1] == 1 and gameBoard[x][y + 2] == 1):
                saveMoveUp()
                y = y + 1  
            else:
                y = y + 1
    return x, y, a, checkHorizontally

def saveMoveLeft(x, y, a, checkHorizontally):
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = True
    else:
        moveList[a][2] = False
    a = a + 1
    
def saveMoveRight(x, y, a, checkHorizotnally):
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = True
    else:
        moveList[a][2] = False
    a = a + 1
    return x, y, a, checkHorizontally

def saveMoveUp(x, y, a, checkHorizontally):
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = True
    else:
        moveList[a][2] = False
    a = a + 1
    return x, y, a, checkHorizontally
    
def saveMoveDown(x, y, a, checkHorizontally):
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = 1
    else:
        moveList[a][2] = 0
    a = a + 1
    moveList
    return x, y, a, checkHorizontally
    
def pickMove(movePickedX, movePickedY, a):
    randomMove = numpy.random.random_integers(0 , a)
#   randomMove = numpy.random.random_integers(b)
    movePickedX = moveList[randomMove - 1][0]
    movePickedY = moveList[randomMove - 1][1]
    return movePickedX, movePickedY, a
    
def executeMove(textFile):
    if(moveList[a][2] == True):
        if(moveList[a][3] == True):
             gameBoard[movePickedX][movePickedY] = 0
             gameBoard[movePickedX + 1][movePickedY] = 0
             gameBoard[movePickedX + 2][movePickedY] = 1
             textFile.write("X: %d , Y: %d to X: %d , Y: %d \n" %(movePickedX, movePickedY, movePickedX + 2, movePickedY))

        if(moveList[a][3] == False):
             gameBoard[movePickedX][movePickedY] = 1
             gameBoard[movePickedX + 1][movePickedY] = 0
             gameBoard[movePickedX + 2][movePickedY] = 0
             textFile.write("X: %d , Y: %d to X: %d , Y: %d \n" %(movePickedX + 2, movePickedY, movePickedX, movePickedY))

    if(moveList[a][2] == False):
        if(moveList[a][3] == False):
             gameBoard[movePickedX][movePickedY] = 0
             gameBoard[movePickedX + 1][movePickedY] = 0
             gameBoard[movePickedX + 2][movePickedY] = 1
             textFile.write("X: %d , Y: %d to X: %d , Y: %d \n" %(movePickedX, movePickedY, movePickedX, movePickedY + 2))

        if(moveList[a][3] == True):
             gameBoard[movePickedX][movePickedY] = 1
             gameBoard[movePickedX + 1][movePickedY] = 0
             gameBoard[movePickedX + 2][movePickedY] = 0
             textFile.write("X: %d , Y: %d to X: %d , Y: %d \n" %(movePickedX, movePickedY + 2, movePickedX, movePickedY))
    return textFile

def evaluate(textFile, x , y):
    pegsLeft = 0
    x = 0
    y = 0
    for i in xrange(0,49):
        if(gameBoard[x][y] == 1):
            pegsLeft = pegsLeft + 1
        if(x < 6):
            x = x + 1
        if(x == 6):
            y = y + 1
            x = 0
    if(pegsLeft == 1):
        if(gameBoard[3][3] == 1):
            textFile.write("SUCCESS! I have solved the game of Peg Solitare!")
            sys.exit()
        else:
            playGame()
    else:
        playRound()        
    return textFile, x, y

    
def playRound(textFile):
    possibleMoves(x, y, a, checkHorizontally)
    pickMove(movePickedX, movePickedY, a)
    executeMove(textFile)
    evaluate(textFile,x,y)
    
def playGame(game):
    game = game + 1
    resetBoard(textFile)
    playRound(textFile)
    
playGame(game)
