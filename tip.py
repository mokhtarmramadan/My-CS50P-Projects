def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Take a stirng meal price and convert it into a float
    n = float(d.replace('$', ''))
    return n


def percent_to_float(p):
    # TODO
    l = float(p.replace('%', ''))
    n = l /100
    return n

main()