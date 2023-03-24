import sys
taqueria ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
counter = 0.00

for taq in taqueria:
    try:
        item = input("Item: ").title()
        if item in taqueria:
            counter += taqueria[item]
            print("Total: $""{:.2f}".format(counter))
    except EOFError:
        print()
        sys.exit()