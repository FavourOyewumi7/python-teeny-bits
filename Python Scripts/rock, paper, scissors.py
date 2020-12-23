import random
import string

name = input('Please enter a name: ')
num = int(input('How many times do you plan on playing this game? '))
print('Welcome {}, This is a Rock, Paper and Scissors game'.format(name))

choices  = ['rock', 'paper', 'scissors']

game = input('Please type in one of Rock, Paper or Scissors: ')
game = game.lower()
if game not in choices:
   raise ValueError( name + ' you have put in a wrong choice ' + game)




def function(game ):
    ge = random.choice(choices)
    
    global score 
    global score1
    score = 0
    score1 = 0
    if game == ge:
        
        print( 'Correct, you have put in '+ game + ' and the computer has put in '
               + ge)
        score = score + 1
        print('Your score is {} : {}'.format(score, score1) )
    else:
        
        print('Awwwwww, you have put in '+ game + ' and the computer has put in '
               + ge +'. Try again' )
        print
        score1 = score1 +1 
        print('Your score is {}: {}'.format(score, score1))

   




function(game)



for i in range(num-1):
    game = input('Please type in one of Rock, Paper or Scissors: ')
    game = game.lower()
    if game not in choices:
       raise ValueError( name + ' you have put in a wrong choice ' + game)
    function(game)
