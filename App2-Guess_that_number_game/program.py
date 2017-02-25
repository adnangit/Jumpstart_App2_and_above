import random

print('-----------------------------')
print('      GUESS THAT NUMBER')
print('-----------------------------')
print()

rand_number = random.randint(0, 100)

guess = -1
name = input('What is your name: ')

while guess != rand_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < rand_number:
        print('Sorry {}, your guess of {} is too LOW'.format(name, guess))
    elif guess > rand_number:
        print('Sorry {}, your guess of {} is too HIGH'.format(name, guess))
    else:
        print('Congratulations {}, your guess is correct!'.format(name))
