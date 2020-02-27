def collatz(number):
	if (number % 2) == 0:
		print(number // 2)
		userNumber = number // 2
		return userNumber # even
	else:
		print(3 * number + 1) # odd
		userNumber = 3 * number + 1
		return userNumber

while True:
	try:
		print('Enter number:')		# ask for a number
		userNumber = int(input())		#
	except NameError: # This should be ValueError but I'm doing something wrong
		print('That is not a number')
		continue
	break

while userNumber > 1:
	userNumber = collatz(userNumber)