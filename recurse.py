def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n - 1)
		result = n * recurse
		#print(n+" * "+recurse+" = "+result)
		#print("%d * %d = %d", n, recurse, result)
		print(n, ' * ', recurse, ' = ', result)
		return result

factorial(4)

def fibonacci(n):
	if n == 0:
		return 0
	elif n==1:
		return 1
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
		print(result)
		return result

#fibonacci(5)