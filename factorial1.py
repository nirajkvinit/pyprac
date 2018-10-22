#factorial
def fact(number):
	if number <= 1:
		return 1
	return number * fact(number -1)

def fact2(number):
	total = 1
	for num in range(1, number+1):
		total = total * num
		#print("{0} = {0} * {1}".format(total, num))
	return total		

if __name__ == '__main__':
	print(fact(5))
	print(fact2(5))