answer = input("What's the answer to the greates question in life, in universe and everything ").lower().strip()

match answer:
    case "42":
        print("Yes")
    case "forty two":
        print("Yes")
    case "forty-two":
        print("Yes")
    case _:
        print("No")