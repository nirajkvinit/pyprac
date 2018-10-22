import random

print('Hello! What is your name?')
name = input()
secretNumber = random.randint(1, 20)

print("Well, " + name + ", I am thinking of a number between 1 & 20. Take a guess")

for guessTaken in range(1, 7):
    print('Take a guess: ')
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good Job! ' + name + '! You guess the number in  ' + str(guessTaken) + ' guess')
else:
    print('Nope! The number I was thinking of was ' + str(secretNUmber))