from twttr import shorten

# Checking if "shorten" handles lower and upper case strings
def test_lower_case():
    assert shorten("lolo") == "ll"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("WhaTsaPp") == "WhTsPp"

# Checking if shorten handles punctuations and numbers
def test_punctuations_and_numbers():
    assert shorten("wha!2/&tsapp") == "wh!2/&tspp"
    assert shorten("fa/*&7cebook") == "f/*&7cbk"
