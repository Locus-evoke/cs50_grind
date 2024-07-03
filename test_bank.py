from bank import value

def test_value_with_hello():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('HELLO') == 0
    assert value('  Hello  ') == 0

def test_value_with_hi():
    assert value('hi') == 20
    assert value('Hi') == 20
    assert value('HI') == 20

def test_value_with_gibberish():
    assert value('fjiowejfiwjo') == 100

def test_value_with_numbers():
    assert value('1234567890') == 100

def test_value_with_raNdOmCaSe():
    assert value('hKskKSalD') == 20
    assert value('Hk') == 20
