import random

random_number = random.randint(1, 10)

guess = None

while True:
    guess = int(input("Guess a number: "))
    if guess > random_number:
        print("Your guess was too high.")
    elif guess < random_number:
        print("Your guess was too low.")
    else:
        print("You guessed correctly!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thanks for playing!")
            break



