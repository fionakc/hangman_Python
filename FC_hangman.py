#SWEN503 - Assignment 1
#Fiona Crook
#300442873

#This programme will play a game of hangman with the user
#The computer will randomly choose a word from the supplied dictionary file
#and will then ask the user to guess the word.
#If the user guesses letters incorrectly, a hangman will appear.
#The game will continue until either the word is correctly guessed,
#or the user has run out of lives.


import sys
import random

##variables to control endgame
gameover = False
didwin = False
livesLeft=12


##read file
with open('dictionarylarge.txt') as fp:
    lines = fp.readlines()  #read data out of file
    words = [x[0:-1] for x in lines] #list words with no endlines

##randomly choose one of the words, convert to upper case
word = random.choice(words).upper() 

##save to list by letter
chosenWord = list(word)

##need list of correct guessed letters - based on word size
correctGuess = []
loop2 = len(chosenWord)
lettersLeftToGuess=len(chosenWord)
#will feed in as many underscores as letters in chosenWord
while loop2>0:
    correctGuess.append('_')
    loop2=loop2-1

##need list of all past guesses
pastGuesses = []
pastGuesses.append(' ')
#give a space, so is already initialised and will loop nicely

#initialise empty hangmanPic 2D array
hangmanPic = [[],[],[],[],[],[],[],[],[]]
loop3 = 0 
while loop3<9:
    hangmanPic.insert(loop3,[' ',' ',' ',' ',' ',' ',' ',' '])
    loop3=loop3+1


#change hangmanPic based on how many lives lost
def loseALife(livesStill):
    global hangmanPic
    if livesStill==11:
        hangmanPic[8][0]='-'
        hangmanPic[8][1]='-'
        hangmanPic[8][2]='-'
        hangmanPic[8][3]='-'
        hangmanPic[8][4]='-'
    if livesStill==10:
        hangmanPic[1][2]='|'
        hangmanPic[2][2]='|'
        hangmanPic[3][2]='|'
        hangmanPic[4][2]='|'
        hangmanPic[5][2]='|'
        hangmanPic[6][2]='|'
        hangmanPic[7][2]='|'
    if livesStill==9:
        hangmanPic[7][3]='\\'
    if livesStill==8:
        hangmanPic[0][2]='_'
        hangmanPic[0][3]='_'
        hangmanPic[0][4]='_'
        hangmanPic[0][5]='_'
        hangmanPic[0][6]='_'
    if livesStill==7:
        hangmanPic[1][3]='/'
    if livesStill==6:
        hangmanPic[1][6]='|'
    if livesStill==5:
        hangmanPic[2][6]='O'
    if livesStill==4:
        hangmanPic[3][6]='|'
        hangmanPic[4][6]='|'
    if livesStill==3:
        hangmanPic[3][5]='-'
    if livesStill==2:
        hangmanPic[3][7]='-'
    if livesStill==1:
        hangmanPic[5][5]='/'
    if livesStill==0:
        hangmanPic[5][7]='\\'

#draw the hangmanPic to terminal
def drawHangmanPic():
    global hangmanPic
    #loop to print out the 2D array
    loop4 = 0
    while loop4 < 10:
        print(' '.join(str(e)for e in hangmanPic[loop4]))   
        loop4=loop4+1

#the start of playing the game
print("This is a word guessing game")
print("You need to correctly guess the letters in the word below before your lives run out")
print("Word to guess:")
print(' '.join(str(e)for e in correctGuess))
print("")

##while not gameover
while not gameover:
    
    ##ask user to guess a letter    
    print("Guess a letter:")
    letterTemp = sys.stdin.readline().strip().upper()
    ##only take first letter offered - trim
    letterGuess = letterTemp[0:1]

    #decisions after letter is guessed
    guessInList=False
    print(" ")

    #check if guess is already in pastGuesses
    for lett in pastGuesses:
        if lett == letterGuess:
            guessInList=True
            break

    ##if guessed before - do nothing
    #only add to pastGuesses if new
    if guessInList:
        print("You have already guessed "+letterGuess)
    else:
        ##if letter in word
        ##and not guessed letter before
        ##replace underscore in correctGuess with letter
        letterInWord = False
        pastGuesses.append(letterGuess)
        for index,lett2 in enumerate(chosenWord):
            if lett2 == letterGuess:
                letterInWord = True
                correctGuess[index]=letterGuess
                lettersLeftToGuess=lettersLeftToGuess-1
                
        ##if letter not in word
        ##and not guessed previously
        ##remove a life
        if not letterInWord:
            print("Sorry, "+letterGuess+" was not in the word")
            livesLeft=livesLeft-1
            loseALife(livesLeft)

    #draw outputs to screen        
    drawHangmanPic()
    print("Word to guess:")
    print(' '.join(str(e)for e in correctGuess))
    print("")
    print("Your previous guesses:")
    print(' '.join(str(e)for e in pastGuesses))
    print("")
    print("**************************************************")
    
    ##check endgame conditions
    if lettersLeftToGuess==0:
        didwin=True
        gameover=True
    
    if livesLeft==0:
        gameover=True

    #end of while loop



##if gameover
##and won - victory
##or lost - commiseration
if didwin:
    print("Congrats, you won!")
    print("You correctly guessed the word "+word)
else:
    print("Sorry, you have lost")
    print("The word you were trying to guess was "+word)
