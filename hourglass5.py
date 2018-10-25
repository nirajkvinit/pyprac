import autopep8


def hourGlassMaxSum(arr):
    maxNum = None
    # oai - outer array index
    # iai - inner array index
    for oai in range(len(arr) - 2):
        for iai in range(len(arr[oai]) - 2):
            curNum = arr[oai][iai]
            curNum += arr[oai][iai + 1]
            curNum += arr[oai][iai + 2]

            curNum += arr[oai + 1][iai + 1]

            curNum += arr[oai + 2][iai]
            curNum += arr[oai + 2][iai + 1]
            curNum += arr[oai + 2][iai + 2]

            if maxNum == None or maxNum < curNum:
                maxNum = curNum

    return maxNum


if __name__ == "__main__":
    arr = []
    # Expected Output
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
    strArr5 = ["-1 1 -1 0 0 0",
               "0 -1 0 0 0 0",
               "-1 -1 -1 0 0 0",
               "0 -9 2 -4 -4 0",
               "-7 0 0 -2 0 0",
               "0 0 -1 -2 -4 0",
               ]
    for strInput in strArr2:
        arr.append(list(map(int, strInput.rstrip().split())))

    print(hourGlassMaxSum(arr))

    # print(arr)
