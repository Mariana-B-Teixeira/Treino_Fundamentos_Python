from plates import is_valid

# Testa função do módulo plates.
def test_Valid():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True

def test_Invalid():
    assert is_valid("A") == False
    assert is_valid("") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("12") == False
    assert is_valid("CS05") == False
    assert is_valid("AAA22A") == False
    assert is_valid("PI3.14") == False
