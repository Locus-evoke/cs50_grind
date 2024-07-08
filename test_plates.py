from plates_improved import is_valid

def test_check_len():
    assert is_valid("AB1234") == True
    assert is_valid("A1234") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("") == False
    assert is_valid("ABCDEF123") == False

def test_check_first_2_letters():
    assert is_valid("AB1234") == True
    assert is_valid("1234AB") == False
    assert is_valid("A1234") == False
    assert is_valid("AB") == True
    assert is_valid("A") == False

def test_check_0():
    assert is_valid("AB0123") == False
    assert is_valid("AB1023") == True
    assert is_valid("AB1230") == True

def test_check_numbers():
    assert is_valid("1234AB") == False
    assert is_valid("A1234") == False
    assert is_valid("1234") == False
    assert is_valid("AB1C4") == False
    assert is_valid("ABCD4") == True

def test_check_special_characters():
    assert is_valid("AB1234") == True
    assert is_valid("AB*234") == False
    assert is_valid("AB!234") == False
    assert is_valid("AB,234") == False
    assert is_valid("AB.234") == False
    assert is_valid("AB?234") == False
    assert is_valid("ABCD") == True
    assert is_valid("1234AB") == False
    assert is_valid("AB_14") == False

def test_mixed_cases():
    assert is_valid("ab1234") == True
    assert is_valid("Ab1234") == True
    assert is_valid("abC12") == True
    assert is_valid("ABC") == True

def test_edge_cases():
    assert is_valid("AB123") == True
    assert is_valid("AB123456") == False
    assert is_valid("AB0CD") == False
