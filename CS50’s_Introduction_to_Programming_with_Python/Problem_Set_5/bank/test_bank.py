from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, how are you?") == 0

def test_h():
    assert value("h") == 20
    assert value("H") == 20

def test_otherwise():
    assert value("David") == 100
    assert value("DAVID") == 100
