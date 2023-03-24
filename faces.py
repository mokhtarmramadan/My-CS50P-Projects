string = input()

for i in range(len(string)):
    if string[i] == ":" and string[i + 1] == ")":
        print("\N{slightly smiling face}", end = '')

    elif string[i] == ":" and string[i + 1] == "(":
        print("\N{slightly frowning face}", end = '')
    elif string[i] == ")" or string[i] == "(":
        continue
    else:
        print(string[i], end ='')
print()