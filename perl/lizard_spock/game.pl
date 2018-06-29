#!/usr/bin/perl
# This a program inspired by the game Rock, Paper, Scissors, Lizard, Spock made popular by the Big Bang Theory
# Gabrielle R. Jameson
# To run type perl lizard_spock.pl followed by a single number (1-5) to choose an attack or 0 to exit


use strict;
use warnings;

# initialze counters to track wins and losses during game play

my $player_win_tracker = 0;
my $player_loss_tracker = 0;


while(1)

{

  # menu for player choices

  print "\n \n Choose your attack. \n ------------------- \n Rock (1) \n Paper (2) \n Scissors (3) \n Lizard (4) \n Spock (5) \n Exit (0) \n ";
  print "------------------- \n";
  my $player_choice = <>;
  chomp($player_choice);

  # random number to assign computer choice

  my $computer_choice =  int(rand(5)) + 1;
  chomp($computer_choice);

  # option to exit game and will display how many games were won and loss by player

  if ($player_choice == 0)

  {
    print "\n \n \nThanks for playing - Live long and prosper! \n";
    print "------------------- \n";
    print "Total number of games player won: ";
    print $player_win_tracker;
    print "\n";
    print "Total number of games player loss: ";
    print $player_loss_tracker;
    print "\n";

    exit;
}

  # display choices made by player and computer

  print "Player chooses: $player_choice and Computer chooses: $computer_choice \n";
  print "------------------------------------------------------- \n";


    # condition to handle ties

    if ( $computer_choice == $player_choice )
    {
       print "It is a tie\n";

    }

    # conditions to handle all game outcome possibilites and track wins/losses for player

    if ($computer_choice == 1 && $player_choice == 4)
    {
       print "Rock crushes lizard!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 4 && $player_choice == 1)
    {
       print "Rock crushes lizard!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 1 && $player_choice == 3)
    {
       print "Rock crushes scissors!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 3 && $player_choice == 1)
    {
       print "Rock crushes scissors!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 2 && $player_choice == 1)
    {
       print "Paper covers rock!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 1 && $player_choice == 2)
    {
       print "Paper covers rock!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 2 && $player_choice == 5)
    {
       print "Paper disproves Spock!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 5 && $player_choice == 2)
    {
     print "Paper disproves Spock!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 3 && $player_choice == 2)
    {
       print "Scissors cut paper!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 2 && $player_choice == 3)
    {
       print "Scissors cut paper!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 3 && $player_choice == 4)
    {
       print "Scissors decapitate lizard!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 4 && $player_choice == 3)
    {
       print "Scissors decapitate lizard!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 4 && $player_choice == 2)
    {
       print "Lizard eats paper!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 2 && $player_choice == 4)
    {
       print "Lizard eats paper!! Player wins! \n";
       $player_win_tracker ++;
    }


    if ($computer_choice == 4 && $player_choice == 5)
    {
       print "Lizard poisons Spock!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 5 && $player_choice == 4)
    {
       print "Lizard poisons Spock!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 5 && $player_choice == 1)
    {
       print "Spock vaporizes rock!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 1 && $player_choice == 5)
    {
       print "Spock vaporizes rock!! Player wins! \n";
       $player_win_tracker ++;
    }

    if ($computer_choice == 5 && $player_choice == 3)
    {
       print "Spock smashes scissors!! Computer wins! \n";
       $player_loss_tracker ++;
    }

    if ($computer_choice == 3 && $player_choice == 5)
    {
       print "Spock smashes scissors!! Player wins! \n";
       $player_loss_tracker ++;
    }






--------------------------------

def evaluateGame(playerChoice, pcChoice):
    #more readable.
    rsp = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    win_statement  = ['Scissors cuts Paper','Paper covers Rock','Rock crushes Lizard','Lizard poisons Spock','Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock Vaporizes Rock', 'Rock crushes Scissors']
    # if player win, win_status = 1 (ex. rock vs scissors -> (1 - 3 == -2) -> (-2 % 3 == 1))
    # if pc win, win_status = 2
    # if tie, win_status = 0
    win_status = (playerChoice - pcChoice) % 5
    print "You have chosen %s" % rsp[playerChoice - 1]
    what_to_say = "Computer has chose %s" % rsp[pcChoice - 1]
    if win_status == 0:
        what_to_say += " as Well. TIE!"
    elif win_status == 1:
        what_to_say += ". %s. You WIN!" % win_statement[playerChoice - 1]
    else:
        what_to_say += ". %s. You LOSE!" % win_statement[pcChoice - 1]
    print what_to_say
    return win_status



    ------

    if pcChoice == 1 and playerChoice == 4:

        print "Rock crushes lizard!! Computer wins! \n";

    if pcChoice == 4 and playerChoice == 1:

        print "Rock crushes lizard!! Player wins! \n";


    if pcChoice == 1 and playerChoice == 3:

        print "Rock crushes scissors!! Computer wins! \n";

    if pcChoice == 3 and playerChoice == 1:

        print "Rock crushes scissors!! Player wins! \n";


    if pcChoice == 2 and playerChoice == 1:

        print "Paper covers rock!! Computer wins! \n";


    if pcChoice == 1 and playerChoice == 2:

        print "Paper covers rock!! Player wins! \n";


    if pcChoice == 2 and playerChoice == 5:

        print "Paper disproves Spock!! Computer wins! \n";


    if pcChoice == 5 and playerChoice == 2:

        print "Paper disproves Spock!! Player wins! \n";


    if pcChoice == 3 and playerChoice == 2:

        print "Scissors cut paper!! Computer wins! \n";


    if pcChoice == 2 and playerChoice == 3:

        print "Scissors cut paper!! Player wins! \n";


    if pcChoice == 3 and playerChoice == 4:

        print "Scissors decapitate lizard!! Computer wins! \n";


    if pcChoice == 4 and playerChoice == 3:

        print "Scissors decapitate lizard!! Player wins! \n";


    if pcChoice == 4 and playerChoice == 2:

        print "Lizard eats paper!! Computer wins! \n";


    if pcChoice == 2 and playerChoice == 4:

        print "Lizard eats paper!! Player wins! \n";



    if pcChoice == 4 and playerChoice == 5:

        print "Lizard poisons Spock!! Computer wins! \n";


    if pcChoice == 5 and playerChoice == 4:

        print "Lizard poisons Spock!! Player wins! \n";


    if pcChoice == 5 and playerChoice == 1:

        print "Spock vaporizes rock!! Computer wins! \n";

    if pcChoice == 1 and playerChoice == 5:

        print "Spock vaporizes rock!! Player wins! \n";


    if pcChoice == 5 and playerChoice == 3:

        print "Spock smashes scissors!! Computer wins! \n";

    if pcChoice == 3 and playerChoice == 5:

        print "Spock smashes scissors!! Player wins! \n";
