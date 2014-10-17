# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 20:34:28 2014

@author: DannyB648
Version: 0.2

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
def resetBoard():
    #global textFile   #Variable defined as you use it, so no need to pre-define textFile.
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
    return textFile
    
def possibleMoves():

    global x
    global y
    global a
    global checkHorizontally
    x = 0
    y = 0
    checkHorizontally = True
    while x < 7 and y < 7:
        checkHorizontally = True
        if(x + 2 == 7):
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
    while(x < 7 and y < 7):
        checkHorizontally = False
        if(y + 2 == 7):
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

def saveMoveLeft():
    global x
    global y
    global a
    global checkHorizontally
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = True
    else:
        moveList[a][2] = False
    a = a + 1
    
def saveMoveRight():
    global x
    global y
    global a
    global checkHorizontally
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = True
    else:
        moveList[a][2] = False
    a = a + 1
    
def saveMoveUp():
    global x
    global y
    global a
    global checkHorizontally
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = True
    else:
        moveList[a][2] = False
    a = a + 1
    
def saveMoveDown():
    global x
    global y
    global a
    global checkHorizontally
    moveList[a][0] = x
    moveList[a][1] = y
    if(checkHorizontally == True):
        moveList[a][2] = 1
    else:
        moveList[a][2] = 0
    a = a + 1
    moveList
    
def pickMove():
    randomMove = 0
    global movePickedX
    global movePickedY
    global a

    if a > 0:
        randomMove = numpy.random.random_integers(a) #pick random number.

    movePickedX = moveList[randomMove][0]
    movePickedY = moveList[randomMove][1]
    
def executeMove(textFile):
#    global textFile
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

def evaluate(textFile):
    global x
    global y
    #global textFile
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
            

    
def playRound(textFile):

    possibleMoves()
    pickMove()
    executeMove(textFile)
    evaluate(textFile)
    
def playGame(game):
    game = game + 1
    txtFile = resetBoard() #variable txtFile now equal to return value of resetBoard. return should be a file object.
    playRound(txtFile)
    
playGame(game)
