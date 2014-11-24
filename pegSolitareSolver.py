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
import sys

"""
Variable Declarations
"""
sys.setrecursionlimit(30000)

movesPossible = 0

yPicked = 0
xPicked = 0
dPicked = 0

move = 0

gameBoard = [[9,9,0,0,0,9,9,],\
                 [9,9,0,0,0,9,9,],\
                 [0,0,1,0,0,0,0,],\
                 [0,0,1,1,1,0,0,],\
                 [0,0,1,0,0,0,0,],\
                 [9,9,0,0,0,9,9,],\
                 [9,9,0,0,0,9,9,]]

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

    gameBoard = [[9,9,1,1,1,9,9,],\
                 [9,9,1,1,1,9,9,],\
                 [1,1,1,1,1,1,1,],\
                 [1,1,1,0,1,1,1,],\
                 [1,1,1,1,1,1,1,],\
                 [9,9,1,1,1,9,9,],\
                 [9,9,1,1,1,9,9,]]   
    return gameBoard

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
            elif(x + 2 < 7 and gameBoard[y][x] == 0 and gameBoard[y][x + 1] == 1 and gameBoard[y][x + 2] == 1):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'h'
                movesPossible = movesPossible + 1
            x = x + 1
        y = y + 1
        
    for y in range(0,5):
        for x in range(0,5):
            if(y + 2 < 7 and gameBoard[y][x] == 1 and gameBoard[y + 1][x] == 1 and gameBoard[y + 2][x] == 0):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'v'
                movesPossible = movesPossible + 1
            elif(y + 2 < 7 and gameBoard[y][x] == 0 and gameBoard[y + 1][x] == 1 and gameBoard[y + 2][x] == 1):
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'v'
                movesPossible = movesPossible + 1
            x = x + 1
        y = y + 1
    
    return movesPossible, gameBoard, movesList

def pickMove(movesPossible, movesList, yPicked, xPicked, dPicked, move):
    move = random.randint(0, movesPossible - 1)
    yPicked = movesList[move][1]
    xPicked = movesList[move][2]
    dPicked = movesList[move][0]
    movesPossible = 0
    return movesPossible, movesList, yPicked, xPicked, dPicked, move

def executeMove(gameBoard, movesList, yPicked, xPicked, dPicked, move, pyPegResults):
    xPicked2 = xPicked + 2
    yPicked2 = yPicked + 2
    xPickedStr = str(xPicked)
    yPickedStr = str(yPicked)
    yPicked2Str = str(yPicked2)
    xPicked2Str = str(xPicked2)
    if(movesList[move][0] == "h"):
        if(gameBoard[yPicked][xPicked] == 0 and gameBoard[yPicked][xPicked + 1] == 1 and gameBoard[yPicked][xPicked + 2] == 1):
            gameBoard[yPicked][xPicked] = 1
            gameBoard[yPicked][xPicked + 1] = 0
            gameBoard[yPicked][xPicked + 2] = 0
            pyPegResults.write("Move from ")
            pyPegResults.write(yPickedStr)
            pyPegResults.write(" , ")
            pyPegResults.write(xPicked2Str)
            pyPegResults.write(" to ")
            pyPegResults.write(yPickedStr)
            pyPegResults.write(" , ")
            pyPegResults.write(xPickedStr)
            pyPegResults.write("\n")
        if(gameBoard[yPicked][xPicked] == 1 and gameBoard[yPicked][xPicked + 1] == 1 and gameBoard[yPicked][xPicked + 2] == 0):
            gameBoard[yPicked][xPicked] = 0
            gameBoard[yPicked][xPicked + 1] = 0
            gameBoard[yPicked][xPicked + 2] = 1
            pyPegResults.write("Move from ")
            pyPegResults.write(yPickedStr)
            pyPegResults.write(" , ")
            pyPegResults.write(xPickedStr)
            pyPegResults.write(" to ")
            pyPegResults.write(xPicked2Str)
            pyPegResults.write(" , ")
            pyPegResults.write(yPickedStr)
            pyPegResults.write("\n")
    elif(movesList[move][0] == "v"):
        if(gameBoard[yPicked][xPicked] == 0 and gameBoard[yPicked + 1][xPicked] == 1 and gameBoard[yPicked + 2][xPicked] == 1):
            gameBoard[yPicked][xPicked] = 1
            gameBoard[yPicked + 1][xPicked] = 0
            gameBoard[yPicked + 2][xPicked] = 0
            pyPegResults.write("Move from ")
            pyPegResults.write(yPicked2Str)
            pyPegResults.write(" , ")
            pyPegResults.write(xPickedStr)
            pyPegResults.write(" to ")
            pyPegResults.write(yPickedStr)
            pyPegResults.write(" , ")
            pyPegResults.write(xPickedStr)
            pyPegResults.write("\n")
        if(gameBoard[yPicked][xPicked] == 1 and gameBoard[yPicked + 1][xPicked] == 1 and gameBoard[yPicked + 2][xPicked] == 0):
            gameBoard[yPicked][xPicked] = 0
            gameBoard[yPicked + 1][xPicked] = 0
            gameBoard[yPicked + 2][xPicked] = 1
            pyPegResults.write("Move from ")
            pyPegResults.write(yPickedStr)
            pyPegResults.write(" , ")
            pyPegResults.write(xPickedStr)
            pyPegResults.write(" to ")
            pyPegResults.write(yPicked2Str)
            pyPegResults.write(" , ")
            pyPegResults.write(xPickedStr)
            pyPegResults.write("\n")
    else:
        print "ERROR, Neither V nor H in MoveList!"
    return gameBoard, movesList, yPicked, xPicked, dPicked, move, pyPegResults


def evaluateBoard(gameBoard, pegSolved, pegsLeft):
    pegsLeft = 0
    for a in range(0,7):
        for b in range(0,7):
            if(gameBoard[a][b] == 1):
                pegsLeft = pegsLeft + 1
            b = b + 1
        a = a + 1
    if(pegsLeft == 1 and gameBoard[3][3] == 1):
        pegSolved == True
    return gameBoard, pegSolved, pegsLeft
        

"""
Actual Sequence
"""


pegSolved = False
gameFinished = False
pegsLeft = 0
pyPegResults = open("pyPegResults.txt","w")
gamesPlayed = 0

def play(pegSolved, gameFinished, movesPossible, gameBoard, movesList, yPicked, xPicked, dPicked, move, pegsLeft, pyPegResults, gamesPlayed):
    while pegSolved == False:
        pyPegResults = open("pyPegResults.txt","w")
        #print"Games Played: ", gamesPlayed
        gameBoard = resetBoard()
        resetMovesList()
        gameFinished = False
        while gameFinished == False:
            movesPossible, gamesBoard, movesList = checkMoves(movesPossible, gameBoard, movesList)
            if(movesPossible == 0):
                
                gameFinished = True
                break
            movesPossible, movesList, yPicked, xPicked, dPicked, move = pickMove(movesPossible, movesList, yPicked, xPicked, dPicked, move)
            gameBoard, movesList, yPicked, xPicked, dPicked, move, pyPegResults = executeMove(gameBoard, movesList, yPicked, xPicked, dPicked, move, pyPegResults)  
        gameBoard, pegSolved, pegsLeft = evaluateBoard(gameBoard, pegSolved, pegsLeft)
        time.sleep(0.00000000000000000000001)

        if(pegsLeft == 1 and gameBoard[3][3] == 1):
            print"SUCCESS"
            pyPegResults.write("Game Won!")
            pyPegResults.write("\n I've Played ")
            gamesPlayed = gamesPlayed + 1
            gamesPlayedStr = str(gamesPlayed)
            pyPegResults.write(gamesPlayedStr)
            pyPegResults.write(" Games before I solved it!")
            pyPegResults.close()
            pegSolved = True
            break
        else:
            pyPegResults.write("Game Lost!")
            pyPegResults.write("\n I've Played ")
            gamesPlayed = gamesPlayed + 1
            gamesPlayedStr = str(gamesPlayed)
            pyPegResults.write(gamesPlayedStr)
            pyPegResults.write(" Games so far!")
            pyPegResults.close()
            #print gameBoard
            #play(pegSolved, gameFinished, movesPossible, gameBoard, movesList, yPicked, xPicked, dPicked, move, pegsLeft, pyPegResults, gamesPlayed)
    print "SUCCESS! Check how to Solve Peg Solitare!"
    return pegSolved
while pegSolved == False: #DEBUG
    if(gamesPlayed == 1000):
        print"I've only played 1000 games so far!
    elif(gamesPlayed == 10000):
        print"I've played 10000 games now!"
    elif(gamesPlayed == 50000):
        print"I've played 50K games and im not done yet!"
    elif(gamesPlayed%10000 == 0 and gamesPlayed > 50000):
        print"Ive played ",gamesPlayed" so far and i'm getting bored!"
        print gameBoard
    pegSolved = play(pegSolved, gameFinished, movesPossible, gameBoard, movesList, yPicked, xPicked, dPicked, move, pegsLeft, pyPegResults, gamesPlayed)
