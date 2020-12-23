import random
import string

name = input('Please enter a name: ')

print('Welcome {}, This is a Rock, Paper and Scissors game'.format(name))

choices  = ['rock', 'paper', 'scissors']

game = input('Please type in one of Rock, Paper or Scissors: ')
game = game.lower()
if game not in choices:
   raise ValueError( name + ' you have put in a wrong choice ' + game)

ge = random.choice(choices)
print('{} played {} and computer played {}'.format(name, game, ge))
if (game == 'rock' and ge == 'scissors')or (game == 'paper' and ge == 'scissors') or (game == 'rock' and ge == 'paper'):
    print('Computer wins')
elif (ge == 'rock' and game == 'scissors')or (ge == 'paper' and game == 'scissors') or (ge == 'rock' and game == 'paper'):
    print('{} win'.format(name))




    
