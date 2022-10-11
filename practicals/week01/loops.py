for i in range(1, 21, 2):
    print(i, end=' ')
print()
# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# c
number_of_star = int(input("number of star:"))
for i in range(number_of_star):
    print('*', end=' ')

# d
number_of_star = int(input("number of star:"))
for i in range(1, number_of_star + 1):
    print('*' * i)
