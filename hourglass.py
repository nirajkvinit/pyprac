import autopep8


class HourGlass:
    arr = []
    hourglassArr = []

    def __init__(self, arr):
        self.arr = arr

    def hourGlassCreator(self):
        arr = self.arr
        outerArrayIndex = 0
        arrMaxIndexIterable = len(arr) - 2
        currentHGNumber = 0
        maxHGNumber = 0

        while outerArrayIndex < arrMaxIndexIterable:
            innerArrayIndex = 0
            while innerArrayIndex < arrMaxIndexIterable:
                str2print = '''
                {ht1} {ht2} {ht3}
                {hm1} {hm2} {hm3}
                {he1} {he2} {he3}
                '''.format(
                    ht1=arr[outerArrayIndex][innerArrayIndex],
                    ht2=arr[outerArrayIndex][innerArrayIndex + 1],
                    ht3=arr[outerArrayIndex][innerArrayIndex + 2],

                    hm1=" ",  # hm1=arr[outerArrayIndex + 1][ht],
                    hm2=arr[outerArrayIndex + 1][innerArrayIndex + 1],
                    hm3=" ",  # hm3=arr[outerArrayIndex + 1][ht + 2],

                    he1=arr[outerArrayIndex + 2][innerArrayIndex],
                    he2=arr[outerArrayIndex + 2][innerArrayIndex + 1],
                    he3=arr[outerArrayIndex + 2][innerArrayIndex + 2]
                )

                innerArrayIndex += 1
                print(str2print)

            # if arrIndex < arrMaxIndex:
            #     arrIndex += 1
            outerArrayIndex += 1


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

    for strInput in strArr:
        arr.append(list(map(int, strInput.rstrip().split())))

    hourglass = HourGlass(arr)
    hourglass.hourGlassCreator()

    # print(arr)
