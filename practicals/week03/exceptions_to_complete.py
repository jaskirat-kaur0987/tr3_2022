"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        """ After adding a valid integer it will come out of while loop"""
        is_finished = True
    except:
        # TODO - add the exception you want to catch after except
        """Error checking for value error"""
        print("Please enter a valid integer.")
print("Valid result is:", result)
