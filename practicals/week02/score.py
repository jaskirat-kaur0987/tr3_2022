"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

import random


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


for i in range(0, 100):
    print(random.randint(0, 100))

main()
