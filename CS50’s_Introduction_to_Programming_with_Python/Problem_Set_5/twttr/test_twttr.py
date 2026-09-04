from twttr import shorten

# Testa função do módulo twttr.
def test_default():
    assert shorten("") == ""

def test_name():
    assert shorten("David CS50.") == "Dvd CS50."
    assert shorten("TWITTER") == "TWTTR"
