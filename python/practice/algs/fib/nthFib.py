print "Find the Nth fibonacci number"


start = int( raw_input("Enter first test number: "))
end = int( raw_input("Enter last test number: "))

def fib(n):
	if n<2:
		return n
	return fib(n-2) + fib(n-1)

print map(fib, range(start, end))
