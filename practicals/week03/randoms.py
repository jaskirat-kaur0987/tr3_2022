import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 1.What did you see on line 1
# Answer: return a random number between 5 and 20, inclusive

# 2.What was the smallest number you could have seen, what was the largest?
# Answer: smallest: 5, largest: 20

# 3.What did you see on line 2?
# Answer: return a random number between 3 and 10, 10 is exclusive.

# 4.What was the smallest number you could have seen, what was the largest?
# Answer: smallest: 3, largest: 9

# 5. Could line 2 have produced a 4?
# Answer: No because step 2 from 3.
#
# 6.What did you see on line 3?
# Answer: a random between 3.5 and 5.5, inclusive

# 7.What was the smallest number you could have seen, what was the largest?
# Answer: smallest:3.5, largest:5.5

# 8.Write code, not a comment, to produce a random number between 1 and 100 inclusive.
# Answer: random.randint(1,100)
for i in range(0,100):
    print(random.randint(1, 100))
