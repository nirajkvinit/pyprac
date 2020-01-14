# Write a program which can compute the given factorial of a number.


def factorial(num):
    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


if __name__ == "__main__":
    print(factorial(int(input("Please enter a number between 1 - 10: "))))
