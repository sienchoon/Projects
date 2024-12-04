import random

#Welcome the player to the game
def main():
    print("Welcome to the guessing game!")

    #assign the values to a variable so that we can call the functions directly in the game
    secret_number = get_secret_number()
    guess = get_guess()
    announce_result(secret_number, guess)

#Generating a random secret number to start the game (range 1-10)
def get_secret_number():
    secret_number = random.randint(1,10)
    return secret_number

#Ask the player to guess a number
def get_guess():
    while True:
        try:
            guess = int(input("Guess a number (1-10): "))
            if guess < 1 or guess > 10:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


#Check if the guess is correct, if True it will congratulate the player, otherwise it will provide the correct answer
def check_guess(secret_number, guess):
    if guess == secret_number:
        return True
    else:
        return False
    
#Announce the result
def announce_result(secret_number, guess):
    if check_guess(secret_number, guess):
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, but the correct number was {secret_number}.")


if __name__ == "__main__":
    main()
