import random
import sys

def play():
    p_choice = input("What do you choose?").capitalize()
    choices = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissors', 4 : 'Lizard', 5 : 'Spock'}
    cpu_choice = choices[random.randint(0,4)]
    if p_choice == cpu_choice:
        return print('Tie!')
    if compare(p_choice,cpu_choice):
        return print('You Win!')
    else:
        return print('You Lose!')

def compare(playerChoice,cpuChoice):
    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False,





               }
    return results[(playerChoice,cpuChoice)]

def game_start():
    begin = input("Would you like to play Rock, Paper, Scissors? Please type Yes or No").capitalize()
    while begin != "Yes":
        if begin == "No":
            print("Game Over")
            sys.exit()
        else:
            print("Please try again")
            begin = input("Would you like to play Rock, Paper, Scissors? Please type Yes or No").capitalize()
    play()
    while True:
        begin = input('Play again? Please type Yes or No').capitalize()
        while begin != "Yes":
            if begin == "No":
                print("Game Over")
                sys.exit()
            else:
                print("Please try again")
                begin = input("Play again? Please type Yes or No").capitalize()
        play()

game_start()



-------


from random import choice

answers = {"yes" : ["yes", "y"],
           "no"  : ["no",  "n"]}

choices = ["rock", "paper", "scissors"]

games = {"win"  : [(choices[0], choices[2]),
                   (choices[1], choices[0]),
                   (choices[2], choices[1])],

         "lose" : [(choices[0], choices[1]),
                   (choices[1], choices[2]),
                   (choices[2], choices[0])],

         "tie"  : [(choices[0], choices[0]),
                   (choices[1], choices[1]),
                   (choices[2], choices[2])]}

print("Let's play \"Rock, paper, scissors\"!\n")

replay = True

while replay:

    player = ""

    while player.lower() not in choices:

        player = input("Rock, paper, or scissors?: ")

    opponent = choice(choices)

    print("You chose {}.".format(player.lower()))
    print("Your opponent chose {}.".format(opponent))

    for outcome in games:

        if (player.lower(), opponent) in games[outcome]:

            print("You {} against your opponent!\n".format(outcome))

    replay_decision = ""

    while replay_decision.lower() not in (answers["yes"] + answers["no"]):

        replay_decision = input("Would you like to play again? [y/n]: ")

        if replay_decision.lower() in answers["no"]:

            replay = False

print("\nThanks for playing!")


-----

#import module
import random

def main():
    #create a variable to control the loop
    play_again = 'y'

    #create a counter for tied games, computer games and player games
    tied_games = 0
    computer_games = 0
    player_games = 0

    #display opening message
    print("Let's play rock, paper scissors!")

    computer_choice = process_computer_choice()

    player_choice = process_player_choice()

    winner = determine_winner(player_choice, computer_choice)

    #setup while loop for playing multiple games
    while play_again == 'y' or play_again == 'Y':

        process_computer_choice()

        process_player_choice()

        #use a if else statement to print the computers choice
        if computer_choice == 1:
            print('computer chooses rock.')

        elif computer_choice == 2:
            print('computer chooses paper.')

        else:
            print('computer chooses scissors.')

            #call the determine winner function
            determine_winner(player_choice, computer_choice)

        #check who won the game and add 1 to the correct counter
        if winner == 'computer':
            computer_games += 1

        elif winner == 'player':
            player_games += 1

        else:
            tied_games += 1

        #ask the user if they would like to play again
        play_again = input('would you like to play again? (enter y for yes): ')

    #display number of games that were won by the computer, the player and that were tied
    print()
    print('there was', tied_games, 'tied games.')
    print('the player won', player_games, 'games.')
    print('The computer won', computer_games,'games.')

#define the process computer function
def process_computer_choice():

    #setup computer to select random integer between 1 and 3
    choice1 = random.randint(1, 3)

    #return the computers choice
    return choice1

#define the process player function
def process_player_choice():

    #add input for players choice
    print()
    print('        MENU')
    print('1) Rock!')
    print('2) Paper!')
    print('3) Scissors!')
    print('4) Quit')
    print()

    player_choice = int(input('Please make a selection:  '))

    #add if statement for quit option
    if player_choice == 4:
        print('Exiting program....')

   #validate if the user enters a correct selection
    while player_choice != 1 and player_choice != 2 and player_choice != 3 and player_choice != 4:

        #print a error message if the wrong selection is entered
        print('Error! Please enter a correct selection.')

        player_choice = int(input('Please make a selection: '))

    #return the players choice
    return player_choice

#define the determine winner function
def determine_winner(player_choice, computer_choice):

    #setup if else statements for each of the 3 computer selections
    if computer_choice == 1:
        if player_choice == 2:
            print('Paper wraps rock. You win!')
            winner = 'player'

        elif player_choice == 3:
            print('Rock smashes scissors. The computer wins!')
            winner = 'computer'

        else:
            print('The game is tied. Try again.')
            winner = 'tied'

    if computer_choice == 2:
        if player_choice == 1:
            print('Paper wraps rock. The computer wins!')
            winner = 'computer'

        elif player_choice == 3:
            print('Scissors cut paper. You win!')
            winner = 'player'

        else:
            print('The game is tied. Try again.')
            winner = 'tied'

    if computer_choice == 3:
        if player_choice == 1:
            print('Rock smashes scissors. You win!')
            winner = 'player'

        elif player_choice == 2:
            print('Scissors cut paper. The computer wins!')
            winner = 'computer'

        else:
            print('The game is tied. Try again.')
            winner = 'tied'

    return winner

main()
