from plates import valid

# Calling the functions
def main():
    test_letters()
    test_lenght()
    test_midnumcase()
    test_zero()
    test_therest()


# Check if all vanity plates start with at least two letters
def test_letters():
    assert valid("CS") == True
    assert valid("H7") == False
    assert valid("3H") == False
    assert valid("35") == False

# Check if vanity plates contain a maximum of 6 characters and a minimum of 2 characters
def test_lenght():
    assert valid("M") == False
    assert valid("OUTATIME") == False
    assert valid("MMMMMM") == True

# Make sure that numbers cannot be used in the middle of a plate, and the numbers don't start with 0. if any
def test_midnumcase():

    assert valid("CS50P") == False
    assert valid("AAA50") == True

# Make sure numbers don't start with zero
def test_zero():
    assert valid("CS05") == False
    assert valid("CS50") == True

# Make sure that there is no periods, spaces, or punctuation
def test_therest():
    assert valid("PI3.14") == False
    assert valid("PI3!14") == False
    assert valid("PI ,14") == False


if __name__ == "__main__":
    main()