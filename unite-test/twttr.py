def main():
    word = str(input("Input: "))
    print(shorten(word))



def shorten(word):
    short = ""
    for i in range(len(word)):
        if word[i].lower() in ['a', 'e','o' , 'i',  'u']:
            continue
        else:
            short += word[i]
    return short

if __name__ == "__main__":
    main()