text = input("Input: ")

for i in range(len(text)):
    if text[i] in ['a', 'e','o' , 'i',  'u', 'A', 'E','O' , 'I',  'U']:
        print("", end ='')
    else:
        print(text[i], end= '')
print()