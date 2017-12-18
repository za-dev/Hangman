import sys
import time
import random
HANGMANPICS = ['''

+---+
|   |
|    
|    
|    
|    
=========''', '''

+---+
|   |
|   O
|   
|   
|  
=========''', '''

+---+
|   |
|   O
|   |
|
|
=========''', '''

+---+
|   |
|   O   
|  /|   
|   
|   
=========''', '''

+---+
|   |
|   O   
|  /|\  
|
|
=========''', '''

+---+
|   |
|   O   
|  /|\  
|  /    
|  
=========''', '''

+----+
|    |
|    O   
|   /|\  
|   / \  
|   
=========''']
def getTheList(no):
    my_dictionary_animals = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    my_dictionary_sports = 'messi ronaldo ibrahimovic henry cristiano marcelo busquets morata dembele iniesta xavi puyol neymar cavani mbappe verrati coutinho cillesen umtiti pique ramos carvajal modric kroos suarez vidal buffon rashford hazard ronaldinho theo isco asensio gomez gotze muller maradona pele ortola townsend willian pedro alves sciglio dybala vitinho ceballos lukaku kane eriksen alli'.split()
    my_dictionary_food = 'oreo burger salami sushi pasta mushrooms cheese butter cream cloves chips oranges noodles cake pastry steak juice idli dosa'.split()
    my_dictionary_history = 'hitler waterloo india commonwealth prussia plassey mountbatten gandhi jhansi'.split()
    printCustom("\nTell me something about your choices.\n")
    printCustom("Pick any one")
    printCustomSlow("... esteemed one.....\n");
    printCustom("1. Sports\n2. Food\n3. Animals\n4. History\n")
    ch=input()
    if(ch=='1'):
        my_dictionary=my_dictionary_sports
    elif(ch=='2'):
        my_dictionary=my_dictionary_food
    elif(ch=='3'):
        my_dictionary=my_dictionary_animals
    elif(ch=='4'):
        my_dictionary=my_dictionary_history
    else:
        printCustom("Sorry. Invalid Choice")
    return(my_dictionary)
def getTheListRepeat(no):
    my_dictionary_animals = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    my_dictionary_sports = 'messi ronaldo ibrahimovic henry cristiano marcelo busquets morata dembele iniesta xavi puyol neymar cavani mbappe verrati coutinho cillesen umtiti pique ramos carvajal modric kroos suarez vidal buffon rashford hazard ronaldinho theo isco asensio gomez gotze muller maradona pele ortola townsend willian pedro alves sciglio dybala vitinho ceballos lukaku kane eriksen alli'.split()
    my_dictionary_food = 'oreo burger salami sushi pasta mushrooms cheese butter cream cloves chips oranges noodles cake pastry steak juice idli dosa'.split()
    my_dictionary_history = 'hitler waterloo india commonwealth prussia plassey mountbatten gandhi jhansi'.split()
    printCustom("1. Sports\n2. Food\n3. Animals\n4. History\n")
    printCustom("Pick any one")
    ch=input()
    if(ch=='1'):
        my_dictionary=my_dictionary_sports
    elif(ch=='2'):
        my_dictionary=my_dictionary_food
    elif(ch=='3'):
        my_dictionary=my_dictionary_animals
    elif(ch=='4'):
        my_dictionary=my_dictionary_history
    else:
        printCustom("Sorry. Invalid Choice")
    return(my_dictionary)
def getRandomWord(wordList):
 
 wordIndex = random.randint(0, len(wordList) - 1)
 return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
 print(HANGMANPICS[len(missedLetters)])
 print()

 print('Missed letters:', end=' ')
 for letter in missedLetters:
     print(letter, end=' ')
 print()

 blanks = '_' * len(secretWord)

 for i in range(len(secretWord)): 
     if secretWord[i] in correctLetters:
         blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

 for letter in blanks: 
     print(letter, end=' ')
 print()

def printCustom(str1):
    for char in str1:
        sys.stdout.write(char)
        time.sleep(0.1)
        
def printCustomSlow(str1):
    for char in str1:
        sys.stdout.write(char)
        time.sleep(0.2)
    
def getGuess(alreadyGuessed):
 
 while True:
     printCustom("Guess a letter.")
     guess = input()
     guess = guess.lower()
             
     if len(guess) != 1:
         printCustom("You have already guessed that letter. Choose again.")
     elif guess in alreadyGuessed:
         printCustom("Please enter a single letter.")
     elif guess not in 'abcdefghijklmnopqrstuvwxyz':
         printCustom("Please enter a LETTER.")
         
     else:
         return guess

def playAgain():
 printCustom("Do you want to play again? (yes or no)")
 return input().lower().startswith('y')


text = "H__A__N__G__M__A__N"
printCustom((text))
my_dictionary = getTheList(1)
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(my_dictionary)
gameIsDone = False

while True:
 displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

 
 guess = getGuess(missedLetters + correctLetters)

 if guess in secretWord:
     correctLetters = correctLetters + guess
            
     foundAllLetters = True
     for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
             foundAllLetters = False
             break
     if foundAllLetters:
         print('Yes! The secret word is "' + secretWord + '"! You have won!')
         gameIsDone = True
 else:
     missedLetters = missedLetters + guess

     
     if len(missedLetters) == len(HANGMANPICS) - 1:
         displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
         print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
         gameIsDone = True

 
 if gameIsDone:
     if playAgain():
         missedLetters = ''
         correctLetters = ''
         gameIsDone = False
         my_dictionary=getTheListRepeat(10)
         secretWord = getRandomWord(my_dictionary)
     else:
         printCustomSlow("Thank you. Hope you enjoyed this.\n")
         printCustomSlow("Signing off.....\n")
         printCustomSlow("Sherwin K Philip")
         break
        

    
