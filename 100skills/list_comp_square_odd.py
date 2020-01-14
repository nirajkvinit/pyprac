'''
Use list comprehension to square each odd number in a list. The list is
input by a sequence of comma-separated numbers.
'''


def list_comp_square(lst):
    return [(x**2) for x in lst if (x % 2 != 0)]


if __name__ == "__main__":
    print(list_comp_square([1, 2, 3, 4, 5, 6, 7, 8, 9]))
