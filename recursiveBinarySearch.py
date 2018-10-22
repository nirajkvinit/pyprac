# Binary search using recursion
def binarySearchRecursive(arr, low, high, value):
	mid = low + int((high + low) / 2)
	
	if arr[mid] == value:
		return mid
	elif arr[mid] < value:
		return binarySearchRecursive(arr, mid + 1, high, value)
	else:
		return binarySearchRecursive(arr, low, mid - 1, value)
	
def binarySearch(arr, value):
	return binarySearchRecursive(arr, 0, len(arr), value)
	
if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8,9]
	print(binarySearch(arr, 5))