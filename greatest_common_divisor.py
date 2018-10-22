# Greatest Common Divisor
# Euclid’s algorithm is used to find gcd. GCD(n,m) == GCD(m, n mod m)
def GCD(mod, number):
	if mod < number:
		return GCD(number, mod)
	if mod % number == 0:
		return number
	return GCD(number, mod % number)

if __name__ == '__main__':
	print(GCD(6, 36))