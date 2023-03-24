camelCase = input("camelCase: ")
snake_case = []

for i in range(len(camelCase)):
    if camelCase[i].isupper():
       snake_case.append("_")
       snake_case.append(camelCase[i].lower())
    else:
        snake_case.append(camelCase[i])

for i in range(len(snake_case)):
    print(snake_c