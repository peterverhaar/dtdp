

number = 17


guess = int( input("Guess a number in between 1 and 50: ") )

while guess != number:

    if guess > number:
        print("Lower!")
    else:
        print("Higher!")
    guess = int( input("Guess again!: ") )

print("The correct number is indeed {}.".format(number) )

