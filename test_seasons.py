from seasons import convert


def test_convert():
    assert convert(323234) == "Four hundred sixty-five million, four hundred fifty-six thousand, nine hundred sixty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
