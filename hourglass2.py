import autopep8


def hourGlassMaxSum(arr):
    oai = 0  # Out Array Index
    outerArrLength = len(arr)   # Array Max iterable index
    curNum = 0  # Current Number
    maxNum = 0  # maximum number
    isNegative = False

    while oai < (outerArrLength - 2):
        iai = 0  # Inner Array Index

        innerArrayIndex = len(arr[oai])
        while iai < (innerArrayIndex - 2):
            # if int(arr[oai][iai]) < 0:
            #     isNegative = True
            # # if isNegative:
            # #     print('is negative')

            curNum += int(arr[oai][iai])
            curNum += int(arr[oai]
                          [iai + 1])
            curNum += int(arr[oai]
                          [iai + 2])

            curNum += int(arr[oai + 1]
                          [iai + 1])

            curNum += int(arr[oai + 2]
                          [iai])
            curNum += int(arr[oai + 2]
                          [iai + 1])
            curNum += int(arr[oai + 2]
                          [iai + 2])

            # print("Curr {} Max {}".format(curNum, maxNum))

            # if isNegative:
            #     if maxNum == 0:
            #         maxNum = curNum
            #     else:
            #         print("1 Curr {} Max {}".format(curNum, maxNum))
            #         if maxNum < curNum:
            #             maxNum = curNum
            #     print("2 Curr {} Max {}".format(curNum, maxNum))
            # else:
            #     if maxNum < curNum:
            #         maxNum = curNum

            if maxNum == 0:
                maxNum = curNum
            elif maxNum < curNum:
                maxNum = curNum

            curNum = 0
            iai += 1

        oai += 1

    return maxNum


if __name__ == "__main__":
    arr = []
    strArr = ["1 1 1 0 0 0",
              "0 1 0 0 0 0",
              "1 1 1 0 0 0",
              "0 0 2 4 4 0",
              "0 0 0 2 0 0",
              "0 0 1 2 4 0"]

    # Expected Output -19
    strArr2 = ["0 -4 -6 0 -7 -6",
               "-1 -2 -6 -8 -3 -1",
               "-8 -4 -2 -8 -8 -6"]

    # Expected Output -6
    strArr3 = ["-1 -1 0 -9 -2 -2",
               "-2 -1 -6 -8 -2 -5",
               "-1 -1 -1 -2 -3 -4"]

    strArr4 = ["1 1 1 0 0 0 1 0",
               "0 1 0 0 0 0 0 1",
               "1 1 1 0 0 0 1 0",
               "0 0 2 4 4 0 0 1"
               ]
    for strInput in strArr2:
        arr.append(list(map(int, strInput.rstrip().split())))

    print(hourGlassMaxSum(arr))

    # print(arr)
