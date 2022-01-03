
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
        if isinstance(start, int) and isinstance(end, int) and start < end:
            break 
        else:
            continue
    return start, end

start, end = user_numbers()
def guess_number(start, end):
    print(start, end)

print(guess_number(start, end))
