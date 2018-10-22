# Binary Search

def binarySearch(arr, value):
	if arr:
		arr.sort()
		print(arr)
		size = len(arr)
		low = 0
		high = size - 1
		
		while low <= high:
			mid = low + int((high - low) / 2)
			if arr[mid] == value:
				return True
			else:
				if arr[mid] < value:
					low = mid + 1
				else:
					high = mid - 1					
	return False

if __name__ == '__main__':
	list1 = [1,10,3,8,5,6,9,4,7,2]
	print(binarySearch(list1, 5))
	print(binarySearch(list1, 11))
	print(binarySearch([], 11))