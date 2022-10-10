# # 1. Basic list operations
numbers = []
for i in range(5):
    valid = False
    while not valid:
        try:
            number = int(input("Number: "))
            numbers.append(number)
            valid = True
        except ValueError as e:
            print("Not a number. Please enter a number")
print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest numbers is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

# # 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
names = str(input(" Enter a name:"))
if names in usernames:
    print("Access Granted")
else:
    print("Access denied")
