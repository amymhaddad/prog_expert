""""
# You'll have to use the following strings:
# 1) "Enter the numerator: "
# 2) "Enter the denominator: "
# 3) "The numerator is not a number."
# 4) "The denominator is not a number."
# 5) "You cannot divide by 0."
# 6) "This division cannot be performed."
# 7) "The result of this division is: _."
# 8) "Goodbye!"

"""

num = input("Enter the numerator: ")
denom = input("Enter the denominator: ") 

try:
    num = float(num)
except Exception:
    print("The numerator is not a number.")

try:
    denom = float(denom)
except Exception:
    print("The denominator is not a number.")

try:
    result = num / denom
    print(f"The result of this division is {result}.")

except ZeroDivisionError:
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
    
except Exception:
    print("This division cannot be performed.")

finally:
    print("Goodbye!")

