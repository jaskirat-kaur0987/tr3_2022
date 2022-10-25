"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


def get_valid_denominator():
    # to avoid the possibility of ZeroDivisionError
    denominator = int(input("Enter a valid denominator: "))
    while denominator <= 0:
        denominator = int(input("Enter a valid denominator: "))
    return denominator


"""

1.When will a ValueError occur? 
Answer - Except the integer, it will show ValueError on any other input. 
2.When will a ZeroDivisionError occur? 
Answer - ZeroDivision only occur when we put denominator as zero.
 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer- To avoid the possibility of ZeroDivisionError,
I added function which passes denominator as a parameter and make sure it's not zero. 

"""
