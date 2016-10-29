# Filename: fib_allN.py
# Written By: Joshua Leihe
# Notes :

def main():
	print "Print all fibonacci numbers from 0 - N"
	goal = input("Enter N: ")
	print "The fibonacci numbers are: "
	n1 = 1
	n2 = 0

	if goal > 0: print 0
	if goal > 1: print 1
	goal = goal - 2	
	while goal > 0:
		goal = goal - 1

		temp = n2
		n2 = n1
		n1 = temp + n1
		print n1

main()
