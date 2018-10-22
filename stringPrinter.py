def stringPrinter(value):
    arrEven = []
    arrOdd = []
    for i in range(len(value)):
        if i == 0 or i % 2 == 0:
            arrEven.append(value[i])
        else:
            arrOdd.append(value[i])
    return "{} {}".format("".join(arrEven), "".join(arrOdd))
numInput = int(input())
while numInput > 0:
	print(stringPrinter(str(input())))
	numInput -= 1


if __name__ == "__main__":
	print(stringPrinter("Hacker"))
	print(stringPrinter("Rank"))
	
	numInput = int(input())
	while numInput > 0:
		print(stringPrinter(str(input())))
		numInput -= 1
		
