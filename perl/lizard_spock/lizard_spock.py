# This a program inspired by the game Rock, Paper, Scissors, Lizard, Spock made popular by the Big Bang Theory
# Gabrielle R. Jameson
# To run type python lizard_spock.pl followed by a single number (1-5) to choose an attack or 0 to exit


import random

class status():
    def __init__(self, name):
        self.tie = 0
        self.player_win = 0
        self.computer_win = 0
        self.name = name

    def get_round(self):
        return self.tie + self.player_win + self.computer_win + 1

# Displays program information, starts main play loop
def main():
    print "Welcome to a game of Rock, Paper, Scissors!"
    print "What would you like to do?"
    print  ""
    game_status  = welcome_menu()
    while True:
        play(game_status)
        end_game(game_status)



def welcome_menu():

    # action for menu selection with input validation

    while True:
        print "[1]: Start New Game"
        print "[2]: Quit"
        print ""
        menu_selection = input("Make a selection: ")
        if menu_selection in [1, 2]:
            break
        else:
            print "Invaild selection -- please try again."

    if menu_selection == 1:
        name = raw_input("What is your name?: ") # raw_input for string
        print "Hello %s." % name
        print "Let's play!"
        game_status = status(name) # initializes a new game
    elif menu_selection == 2: # exits game
        print "Thanks for playing -- Live long and prosper!"
        exit()
        return

    return game_status


# displays the menu for user, if input == 3, program is exited
# reads in generated computer choice, outcome from the game play and keeps track of wins for each player

def play(game_status):
    player_choice = int(player_menu())
    computer_choice = computer_choice_generator()
    outcome = game_evaluator(player_choice, computer_choice)
    update_scoreboard(outcome, game_status)


# prints the menu calls in validation if needed
# the input is not valid will loop and continue to ask for validation


def player_menu():
    print "Choose your attack: \n [1]: Rock \n [2]: Paper \n [3]: Scissors \n [4]: Lizard \n [5]: Spock \n "
    menu_selection = input("What will it be? ")
    while not input_validation(menu_selection):
        invalid_choice(menu_selection) # if the menu selection is not within range causes validation check
        menu_selection = input("Enter a correct value: ")
    return menu_selection


# check for input validation

def input_validation(menu_selction):
    if menu_selction in [1, 2, 3, 4, 5]: # more readable.
        return True
    else:
        return False


# generates a random integer 1-5 to determine computer selection

def computer_choice_generator():
    computer_choice = random.randint(1,5)
    return computer_choice


# evaluate if the winner is pc or player or tie, return value accordingly and phrasing

def game_evaluator(player_choice, computer_choice):
    if player_choice == computer_choice:
        win_status = 0
        print "Its a tie!"
    elif player_choice == 4 and computer_choice == 1:
        win_status = 2
        print "Rock crushes lizard!! Computer wins! \n"
    elif player_choice == 1 and computer_choice == 4:
        win_status = 1
        print "Rock crushes lizard!! Player wins! \n"
    elif player_choice == 3 and computer_choice == 1:
        win_status = 2
        print "Rock crushes scissors!! Computer wins! \n"
    elif player_choice == 1 and computer_choice == 3:
        win_status = 1
        print "Rock crushes scissors!! Player wins! \n"
    elif player_choice == 1 and computer_choice == 2:
        win_status = 2
        print "Paper covers rock!! Computer wins! \n"
    elif player_choice ==2 and computer_choice == 1:
        win_status = 1
        print "Paper covers rock!! Player wins! \n"
    elif player_choice == 5 and computer_choice == 2:
        win_status = 2
        print "Paper disproves Spock!! Computer wins! \n"
    elif player_choice == 2 and computer_choice == 5:
        win_status = 1
        print "Paper disproves Spock!! Player wins! \n"
    elif player_choice == 2 and computer_choice == 3:
        win_status = 2
        print "Scissors cut paper!! Computer wins! \n"
    elif player_choice == 3 and computer_choice == 2:
        win_status = 1
        print "Scissors cut paper!! Player wins! \n"
    elif player_choice == 4 and computer_choice == 3:
        win_status = 2
        print "Scissors decapitate lizard!! Computer wins! \n"
    elif player_choice == 3 and computer_choice == 4:
        win_status = 1
        print "Scissors decapitate lizard!! Player wins! \n"
    elif player_choice == 2 and computer_choice == 4:
        win_status = 2
        print "Lizard eats paper!! Computer wins! \n"
    elif player_choice == 4 and computer_choice == 2:
        win_status = 1
        print "Lizard eats paper!! Player wins! \n"
    elif player_choice == 5 and computer_choice == 4:
        win_status = 2
        print "Lizard poisons Spock!! Computer wins! \n"
    elif player_choice == 4 and computer_choice == 5:
        win_status = 1
        print "Lizard poisons Spock!! Player wins! \n"
    elif player_choice == 1 and computer_choice == 5:
        win_status = 2
        print "Spock vaporizes rock!! Computer wins! \n"
    elif player_choice == 5 and computer_choice == 1:
        win_status = 1
        print "Spock vaporizes rock!! Player wins! \n"
    elif player_choice == 3 and computer_choice == 5:
        print "Spock smashes scissors!! Computer wins! \n"
    elif player_choice == 5 and computer_choice == 3:
        win_status = 1
        print "Spock smashes scissors!! Player wins! \n"
    return win_status


# keeps track of ties, player wins, and computer wins

def update_scoreboard(outcome, game_status):
    if outcome == 0:
        game_status.tie += 1
    elif outcome == 1:
        game_status.player_win += 1
    else:
        game_status.computer_win += 1

# If user input is invalid, print a reminder

def invalid_choice(menu_selection):
    print menu_selection, "is not a valid option. Please use 1-3"


# Print the scores before terminating the program.

def display_scoreboard(game_status):
    print ""
    print "Statistics: "
    print "Ties: %d" % game_status.tie
    print "Player Wins: %d" % game_status.player_win
    print "Computer Wins: %d" % game_status.computer_win
    print "Rounds: %d" % game_status.get_round()

# At the end of each game play show user the menu selection

def end_game(game_status):
    print ""
    print "[1]: Play again"
    print "[2]: Show Statistics"
    print "[3]: Quit"
    print ""
    while True:
        menu_selection = input("Enter choice: ")
        if menu_selection in [1, 2, 3]:
            break
        else:
            print "Wrong input -- please try again." # catch if input is not 1-3

    if menu_selection == 2:
        display_scoreboard(game_status)
        end_game(game_status)
    elif menu_selection == 3:
        print "Bye!"
        exit()
main()
