'''
Write a program which will find all the numbers which are divisible by
7 but are not a multiple of 5, between 1000 and 1500 (both included). The
numbers obtained should be printed in a comma-separated sequence on a single
line.
'''


def div_by_7_not_multiple_of_5():
    found_number = []
    for i in range(1000, 1500+1):
        if i % 7 == 0 and i % 5 != 0:
            found_number.append(str(i))

    return ','.join(found_number)


if __name__ == "__main__":
    print(div_by_7_not_multiple_of_5())
