import random

takenGuesses = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while takenGuesses < 5:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    takenGuesses += 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    takenGuesses = str(takenGuesses)
    print('Good job, ' + name + '! You guessed my number in ' + takenGuesses + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was' + number)
    