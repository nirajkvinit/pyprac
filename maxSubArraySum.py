def maxSubArraySum(arr):
	size = len(arr)
	maxSoFar = 0
	maxEndHere = 0
	i = 0
	while i < size:
		maxEndHere = maxEndHere + arr[i]
		#print(arr[i], maxEndHere, maxSoFar)
		if maxEndHere < 0:
			maxEndHere = 0
		if maxSoFar < maxEndHere:
			maxSoFar = maxEndHere
		i += 1
	return maxSoFar

if __name__ == '__main__':
	arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
	print(maxSubArraySum(arr))
	arr2 = [-2,-5,6,-2,-3,1,5,-6]
	print(maxSubArraySum(arr2))