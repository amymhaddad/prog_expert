import random

def user_numbers():
    start = 0
    end = 0
    while True:
        try:
            start = int(input("Enter the start of the range: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
   
        while end < start:
            try:
                end = int(input("Enter the end of the range: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            finally:
                if end < start:
                    print("Please enter a valid number.")
                    continue
        if start < end:
            break 

    return start, end

def guess_number():
    start, end = user_numbers()
    attempts = 1
    random_num = random.randint(start, end)
    guessed_num = ""
   
    while True:
        try:
            guessed_num = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        guessed_num = int(guessed_num)
        break

    while random_num != int(guessed_num):
        guessed_num = input("Guess a number: ")
        attempts += 1

    if attempts > 1:
        print(f"You guessed the number in {attempts} attempts")
    else:
        print(f"You guessed the number in {attempts} attempt")
guess_number()
