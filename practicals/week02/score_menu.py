# get valid score from 0 to 100, 100 is inclusive

for i in range(0, 101, 1):
    print(f"{i:1}")


# print result (copy or import your function from score.py)
def main():
    score = float(input("Enter score: "))
    get_score(score)


def get_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


# print stars as many as the score
score = int(input("Enter score:"))
for i in range(1, score + 1):
    print('*' * i)

main()
# quit
print("quit")
