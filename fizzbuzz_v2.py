while True:
	try:
		n = int(raw_input('please enter a number you would like to count to: '))
		break
	except:
		print 'you need to enter a number, please'

print "fizz buzz counting up to "+str(n)

n = n + 1
for x in range(1, n):
	if x%3 == 0 and x%5 == 0:
		print 'fizz buzz'
	elif x%3 == 0:
		print 'fizz'
	elif x%5 == 0:
		print 'buzz'
	else:
		print x

		# use specific exception on line 5
		# another way to handle the while/try/except block