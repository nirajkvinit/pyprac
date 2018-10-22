def decimalToBinarySimple(number):
    binaryString = ""
    while number > 0:
        binaryString += str(number % 2)
        number = number // 2

    return binaryString

def decimalToBinaryRecursive(number):
    if number > 0:
        return binary2(number // 2) + str(number % 2)
    else:
        return '0'

def consecutiveOne(strInput):
    consecutive = 0
    maxConsecutive = 0
    for i in strInput:
        if int(i) == 1:
            consecutive += 1
        else:
            if consecutive > maxConsecutive:
                maxConsecutive = consecutive
            consecutive = 0

    if consecutive > maxConsecutive:
        maxConsecutive = consecutive

    return maxConsecutive

if __name__ == "__main__":
    print(decimalToBinary(5))
    print(binary2(5))
    print(binary2(13))
    print(consecutiveOne(binary2(5)))
    print(consecutiveOne(binary2(13)))
    print(consecutiveOne('00001'))
