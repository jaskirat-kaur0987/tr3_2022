total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total = total + price

if total > 100:
    total = total * 0.9  # apply 10% discount

print("Total price for {} items is ${:.2f}".format(number_of_items, total))
