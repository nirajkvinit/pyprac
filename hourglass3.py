import autopep8


def hourGlassMaxSum(arr):
    oai = 0  # Out Array Index
    outerArrLength = len(arr)    # Array Max iterable index
    curNum = 0  # Current Number
    maxNum = 0  # maximum number

    while oai < (outerArrLength - 2):
        iai = 0  # Inner Array Index
        str2print = ""
        innerArrLength = len(arr[oai])
        while iai < (innerArrLength - 2):
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

            str2print += '''
                {ht1} {ht2} {ht3}
                {hm1} {hm2} {hm3}
                {he1} {he2} {he3}
                '''.format(
                ht1=arr[oai][iai],
                ht2=arr[oai][iai + 1],
                ht3=arr[oai][iai + 2],

                # hm1=arr[oai + 1][iai],
                hm1=" ",
                hm2=arr[oai + 1][iai + 1],
                # hm3=arr[oai + 1][iai + 2],
                hm3=" ",

                he1=arr[oai + 2][iai],
                he2=arr[oai + 2][iai + 1],
                he3=arr[oai + 2][iai + 2],
            )

            iai += 1
        print(str2print)
        oai += 1

    return maxNum


if __name__ == "__main__":
    arr = []

    # Expected Output 19
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

    hourGlassMaxSum(arr)

    # print(arr)
