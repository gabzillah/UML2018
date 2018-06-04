#!/usr/bin/perl
# This program takes in strings and sorts them alphabetically
# Gabrielle R. Jameson
# To run type perl sort.pl followed by two or more strings

use strict;
use warnings;

# declare an array take in user input
# note that my was used to restrict scope of variable
my @user_input = @ARGV;

# pop off first arg and set it to action(var where if statement)
# an exception to throw error if input was less than two strings
if (@user_input < 2)
{
  die "Invalid command line arguments to program. Please supply two or more strings
      to sort.\n";
}
# if statement if -r || --reverse do action of reverse sort and exit gracely - check that exit 0




# use sort function
@user_input = sort @user_input;

# foreach loop to print out alphabetized list
foreach my $word(@user_input)
{
  print "$word ";
}
