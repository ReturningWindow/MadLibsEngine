import random

GUESS_LIMIT = random.randint(1, 10)

def obtain_number():
    input_number = input("Type a number: ")
    if input_number.isdigit():
        input_number = int(input_number)
        if input_number <= 0:
            print("Please type a number larger than 0 next time.")
            quit()
    else:
        print("Please type a number next time.")
        quit()

    return input_number

def main():
    max_number = obtain_number()
    computer_number = random.randint(0, max_number)
    count = 0 

    while count < GUESS_LIMIT:
        print(f"You have to guess the number in {GUESS_LIMIT} times!")
        print(f"You have {GUESS_LIMIT - count} chances remaining!")
        try:
            guess = int(input(f"Guess a number between 0 - {max_number} "))
        except ValueError:
            print(f"This {guess} is not a valid number! Try again...")
            continue

        if guess > computer_number:
            print(f"{guess} is way to high!")
            count += 1
        elif guess < computer_number:
            print(f"{guess} is way to low!")
            count += 1
        else: 
            print(f"Good job! You managed to find out the number was {computer_number}!\nThanks for playing!")
            quit()
    
    print(f"It looks like you failed! I will give you the number that I thought of {computer_number}. Please try again")


if __name__ == '__main__':
    main()

