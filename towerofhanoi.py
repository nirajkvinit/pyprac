#towerofhanoi

def towerofhanoi(number, source, destination, temp):
	if number < 1:
		return
	towerofhanoi(number - 1, source, temp, destination)
	print("Move {0} disk from {1} to {2}".format(number, source, destination))
	towerofhanoi(number - 1, temp, destination, source)
	
if __name__ == '__main__':
	print(towerofhanoi(3, 'A', 'C', 'B'))