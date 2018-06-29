# This program takes in strings and sorts them alphabetically
# Gabrielle R. Jameson
# To run type python sort.py

# import system-specific parameters and functions in order to invoke sys.argv
# sys.argv basically a function that creates an array to hold the command line arguments of the program
# if statement to check that user inputs more than two strings to sort
 # user input is put into an array and sorted alphabetically using a for loop


# use split() so first need to check if the user input (word) has


import sys

pname = sys.argv[0]
if(len(pname) < 3 ):
   print "Invalid command line arguments to program.Please supply two or more strings to sort."
else :
   for i in sorted(sys.argv):
      if(i != pname):
         print i,
for word in string.split():
    if(word.count(word) == 2):
        print "Invalid command line"
