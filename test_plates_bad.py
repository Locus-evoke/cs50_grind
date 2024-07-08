from plates_improved import is_valid

def test_plate_checker_with_normal():
    assert is_valid('hello') == True

def test_plate_checker_with_CAPITALS():
    assert is_valid('GDEGDH') == True

def test_plate_checker_with_special_symbols():
    assert is_valid('cs50#$') == False

def test_plate_checker_with_only_numbers():
    assert is_valid('32340') == False

def test_plate_checker_with_text_and_nums():
    assert is_valid('33ed') == False
    assert is_valid('ed34') == True

def test_plate_checker_with_only_spec_characs():
    assert is_valid('!@#$%') == False

def test_plate_checker_with_long_stuff():
    assert is_valid('cshfwufewifu') == False
    assert is_valid('cshfwufewifu2132321') == False
    assert is_valid('1231cshfwu') == False
    assert is_valid('1231#$%^cu') == False








