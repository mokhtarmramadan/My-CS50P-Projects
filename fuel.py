while True:
    feul = input("Fruaction: ")
    x = feul.split("/")
    if x[0].isdigit() and x[1].isdigit() and int(x[1]) != 0 and int(x[0]) <= int(x[1]):
        break

y = round((int(x[0]) / int(x[1])) * 100)
if y == 100 or y == 99:
    print("F")
elif y == 0 or y == 1:
    print("E")
else:
    print(f"{y}%")