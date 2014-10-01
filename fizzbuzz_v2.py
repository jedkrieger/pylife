n = raw_input('please enter a number you would like to count to: ')

print "fizz buzz counting up to"+n

n = int(n) + 1
for n in range(1, n):
	if n%3 == 0 and n%5 == 0:
		print 'fizz buzz'
	elif n%3 == 0:
		print 'fizz'
	elif n%5 == 0:
		print 'buzz'
	else:
		print n