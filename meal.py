def main():
    time = input("what time is it: ").strip()
    convert(time)


def convert(time):
    hour = time.split(":")
    if hour[0] == '7' or hour[0] =='8' and hour[1] == '00':
        print("breakfast time")
    elif hour[0] == '12' or hour[0] =='13' and hour[1] == '00':
        print("lunch time")
    elif hour[0] == '18' or hour[0] =='19' and hour[1] == '00':
        print("dinner time")
    else:
        return


if __name__ == "__main__":
    main()