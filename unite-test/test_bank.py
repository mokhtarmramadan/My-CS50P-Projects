from bank import value

# Checking "hello" with all lettercases
def test_hello():
    assert value("hello luna") == "$0"
    assert value("Hello") == "$0"
    assert value("HeLLo, Mo") == "$0"

# Checking "h" with all cases
def test_h():
    assert value("him") == "$20"
    assert value("How") == "$20"

# Checking other letters and words
def test_rest():
    assert value("What's") == "$100"
    assert value("what's hello") == "$100"