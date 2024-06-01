from twttr import shorten

vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def test_words():
    assert  shorten("twitter") == "twttr"
    assert  shorten("CS50") == "CS50"
    assert  shorten("Twitter") == "Twttr"
    assert  shorten("PYTHON") == "PYTHN"
    assert  shorten("What's your name?") == "Wht's yr nm?"
    assert  shorten("hell0/") == "hll0/"
