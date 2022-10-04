numbers = [3, 1, 4, 1, 5, 9, 2]
# number[0] = 3
# numbers[-1] = 2
print(numbers[-1])
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers is True
# 7 in numbers is False
# "3" in numbers is False
# numbers + [6, 5, 3]) = [3, 1, 4, 1, 5, 9, 6, 5, 3]
print(numbers + [6, 5, 3])


# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Get all the elements from numbers except the first two (slice)
new_number = numbers[2:]
print(new_number)
# Check if 9 is an element of numbers
print(9 in numbers)
