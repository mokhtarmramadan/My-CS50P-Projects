string = input()
for i in range(len(string)):
    if string[i] == " ":
        print("...", end ='')
    else:
        print(string[i], end = '')
print()