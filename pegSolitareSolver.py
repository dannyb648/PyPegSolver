# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 20:34:28 2014

@author: DannyB648
Version: 0.3

Purpose of this script is to play games of Peg Solitaire randomly until it successfully
completes the game. It will then print out the successful game moves to a .txt file.
"""

import random

gameBoard = [[9,9,1,1,1,9,9,],\
             [9,9,1,1,1,9,9,],\
             [1,1,1,1,1,1,1,],\
             [1,1,1,0,1,1,1,],\
             [1,1,1,1,1,1,1,],\
             [9,9,1,1,1,9,9,],\
             [9,9,1,1,1,9,9,]]

movesPossible = 0

yPicked = 0
xPicked = 0
dPicked = 0
              
movesList = [[9,9,9],\
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
    for y in range(0,5):
        for x in range(0,5):
            if(gameBoard[y][x] == 1 and gameBoard[y][x + 1] == 1 and gameBoard[y][x + 2] == 0):
                movesPossible = movesPossible + 1
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'h'
                print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            elif(gameBoard[y][x] == 0 and gameBoard[y][x + 1] == 1 and gameBoard[y][x + 2] == 1):
                movesPossible = movesPossible + 1
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'h'
                print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            x = x + 1
        y = y + 1
        
    for y in range(0,5):
        for x in range(0,5):
            if(gameBoard[y][x] == 1 and gameBoard[y + 1][x] == 1 and gameBoard[y + 2][x] == 0):
                movesPossible = movesPossible + 1
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'v'
                print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            elif(gameBoard[y][x] == 0 and gameBoard[y + 1][x] == 1 and gameBoard[y + 2][x] == 1):
                movesPossible = movesPossible + 1
                movesList[movesPossible][1] = y
                movesList[movesPossible][2] = x
                movesList[movesPossible][0] = 'v'
                print movesList[movesPossible][1], movesList[movesPossible][2] #DEBUG
            x = x + 1
        y = y + 1
    print movesPossible
    return movesPossible, gameBoard, movesList

def pickMove(movesPossible, movesList, yPicked, xPicked, dPicked):
    move = random.randint(0, movesPossible)
    print move
    yPicked = movesList[move][1]
    xPicked = movesList[move][2]
    dPicked = movesList[move][0]
    return yPicked, xPicked

