from twttr import shorten

def test_default():
    assert shorten("") == ""

def test_name():
    assert shorten("David CS50.") == "Dvd CS50."
    assert shorten("TWITTER") == "TWTTR"
