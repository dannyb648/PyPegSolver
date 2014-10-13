# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 20:34:28 2014

@author: DannyB648

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

gameBoard = numpy.array(range(49)).reshape((7, 7))
moveList = numpy.array(range(66)).reshape((33,2))
# Key for gameBoard Array: 0 = Empty, 1 = Peg, 2 = Void.


x = 0
y = 0
a = 0
movePickedX = 0
movePickedY = 0
    
def resetBoard():
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
    
def possibleMoves():

    global x
    global y
    global a
    x = 0
    y = 0
    while x < 7 and y < 7:
        if(x + 2 == 7):
            y = y + 1
        else:
            if(gameBoard[x][y] == 1 and gameBoard[x + 1][y] == 1 and gameBoard[x + 2][y] == 0):
                saveMove()
                x = x + 1
            elif(gameBoard[x][y] == 0 and gameBoard[x + 1][y] == 1 and gameBoard[x + 2][y] == 1):
                saveMove()
                x = x + 1
            else:
                x = x + 1
    while(x < 7 and y < 7):
        if(y + 2 == 7):
            x = x + 1
        else:
            if(gameBoard[x][y] == 1 and gameBoard[x][y + 1] == 1 and gameBoard[x][y + 2] == 0):
                saveMove()
                y = y + 1
            elif(gameBoard[x][y] == 0 and gameBoard[x][y + 1] == 1 and gameBoard[x][y + 2] == 1):
                saveMove()
                y = y + 1  
            else:
                y = y + 1

def saveMove():
    
    global x
    global y
    global a
    moveList[a][0] = x
    moveList[a][1] = y
    a = a + 1
    
def pickMove():
    randomMove = 0
    global movePickedX
    global movePickedY
    global a
    randomMove = numpy.random(0,a)
    movePickedX = moveList[randomMove][0]
    movePickedY = moveList[randomMove][1]
    
def executeMove():
