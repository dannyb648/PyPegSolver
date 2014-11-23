# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 20:34:28 2014

@author: DannyB648
Version: 0.3

Purpose of this script is to play games of Peg Solitaire randomly until it successfully
completes the game. It will then print out the successful game moves to a .txt file.
"""

import random
import time

"""
Variable Declarations
"""


movesPossible = 0

yPicked = 0
xPicked = 0
dPicked = 0

move = 0

gameBoard = [[9,9,1,1,1,9,9,],\
            [9,9,1,1,1,9,9,],\
            [1,1,1,1,1,1,1,],\
            [1,1,1,0,1,1,1,],\
            [1,1,1,1,1,1,1,],\
            [9,9,1,1,1,9,9,],\
            [9,9,1,1,1,9,9,]]

movesList = [[9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9]]

"""
Functions
"""

def resetBoard():
    gameBoard = [[9,9,0,0,0,9,9,],\
                 [9,9,0,0,0,9,9,],\
                 [0,0,0,0,0,0,0,],\
                 [0,0,0,1,0,0,0,],\
                 [0,0,0,0,0,0,0,],\
                 [9,9,0,0,0,9,9,],\
                 [9,9,0,0,0,9,9,]]

def resetMovesList():
    movesList = [[9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9],\
                 [9,9,9]]

def checkMoves(movesPossible, gameBoard, movesList):
    for y in range(0,7):
        for x in range(0,7):
            if(x + 2 < 7 and gameBoard[y][x] == 1 and gameBoard[y][x + 1] == 1 and gameBoard[y][x + 2] == 0):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'h'
                movesPossible = movesPossible + 1
                #print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            elif(x + 2 < 7 and gameBoard[y][x] == 0 and gameBoard[y][x + 1] == 1 and gameBoard[y][x + 2] == 1):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'h'
                movesPossible = movesPossible + 1
                #print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            x = x + 1
        y = y + 1
        
    for y in range(0,5):
        for x in range(0,5):
            if(y + 2 < 7 and gameBoard[y][x] == 1 and gameBoard[y + 1][x] == 1 and gameBoard[y + 2][x] == 0):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'v'
                movesPossible = movesPossible + 1
                #print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            elif(y + 2 < 7 and gameBoard[y][x] == 0 and gameBoard[y + 1][x] == 1 and gameBoard[y + 2][x] == 1):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'v'
                movesPossible = movesPossible + 1
                #print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            x = x + 1
        y = y + 1
    print "movesPossible = ",movesPossible
    
    return movesPossible, gameBoard, movesList

def pickMove(movesPossible, movesList, yPicked, xPicked, dPicked, move):
    move = random.randint(0, movesPossible - 1)
    yPicked = movesList[move][1]
    xPicked = movesList[move][2]
    dPicked = movesList[move][0]
    movesPossible = 0
    return movesPossible, movesList, yPicked, xPicked, dPicked, move

def executeMove(gameBoard, movesList, yPicked, xPicked, dPicked, move):
    if(movesList[move][0] == "h"):
        if(gameBoard[yPicked][xPicked] == 0 and gameBoard[yPicked][xPicked + 1] == 1 and gameBoard[yPicked][xPicked + 2] == 1):
            gameBoard[yPicked][xPicked] = 1
            gameBoard[yPicked][xPicked + 1] = 0
            gameBoard[yPicked][xPicked + 2] = 0
            print "Horizontal Take Right" #DEBUG
        if(gameBoard[yPicked][xPicked] == 1 and gameBoard[yPicked][xPicked + 1] == 1 and gameBoard[yPicked][xPicked + 2] == 0):
            gameBoard[yPicked][xPicked] = 0
            gameBoard[yPicked][xPicked + 1] = 0
            gameBoard[yPicked][xPicked + 2] = 1
            print "Horizontal Take Left" #DEBUG
    elif(movesList[move][0] == "v"):
        if(gameBoard[yPicked][xPicked] == 0 and gameBoard[yPicked + 1][xPicked] == 1 and gameBoard[yPicked + 2][xPicked] == 1):
            gameBoard[yPicked][xPicked] = 1
            gameBoard[yPicked + 1][xPicked] = 0
            gameBoard[yPicked + 2][xPicked] = 0
            print "Vertical Take Up" #DEBUG
        if(gameBoard[yPicked][xPicked] == 1 and gameBoard[yPicked + 1][xPicked] == 1 and gameBoard[yPicked + 2][xPicked] == 0):
            gameBoard[yPicked][xPicked] = 0
            gameBoard[yPicked + 1][xPicked] = 0
            gameBoard[yPicked + 2][xPicked] = 1
            print "Vertical Take Down" #DEBUG
    else:
        print "ERROR, Neither V nor H in MoveList!"
    return gameBoard, movesList, yPicked, xPicked, dPicked, move


def evaluateBoard(gameBoard, pegSolved):
    pegsLeft = 0
    for a in range(0,7):
        for b in range(0,7):
            if(gameBoard[a][b] == 1):
                pegsLeft = pegsLeft + 1
            b = b + 1
        a = a + 1
    if(pegsLeft == 1 and gameBoard[3][3] == 1):
        pegSolved == True
    print"Pegs Left: ",pegsLeft
    return gameBoard, pegSolved
        

"""
Actual Sequence
"""
pegSolved = False
gameFinished = False

while pegSolved == False:
    resetBoard()
    resetMovesList()
    while gameFinished == False:
        movesPossible, gamesBoard, movesList = checkMoves(movesPossible, gameBoard, movesList)
        if(movesPossible == 0):
            print"END"
            gameFinished = True
            break
        movesPossible, movesList, yPicked, xPicked, dPicked, move = pickMove(movesPossible, movesList, yPicked, xPicked, dPicked, move)
        gameBoard, movesList, yPicked, xPicked, dPicked, move = executeMove(gameBoard, movesList, yPicked, xPicked, dPicked, move)  
    gameBoard, pegSolved = evaluateBoard(gameBoard, pegSolved)
    print gameBoard
    print pegSolved
    time.sleep(2)
    if(pegSolved == True):
        break

print "SUCCESS! Check how to Solve Peg Solitare!"
