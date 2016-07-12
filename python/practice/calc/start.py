# File Name: calc.py
# Written By: Joshua Leihe
# Purpose: Create a simple python script that takes a string input and translates it to a mathematical equation.  The script should then return the result (or an explanation as to why there was an error).

from utils import *

print "\nWelcome to Calc 0.1!"
print "Enter \"h\"for help and detailed list of commands!\n\n"
eq_str = raw_input("Calc 0.1 >> ")
print "The equation entered was " + eq_str
