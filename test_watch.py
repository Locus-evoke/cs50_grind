from watch import parse

def test_parse():
    assert parse('<iframe src="https://www.youtube.com/embed/abc123"') == "https://youtu.be/abc123"
    assert parse('<iframe src="https://www.youtube.com/embed/XYZ789"') == "https://youtu.be/XYZ789"
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/123ABC"') == "https://youtu.be/123ABC"
    assert parse('<iframe src="https://www.youtube.com/embed/moreText123"') == "https://youtu.be/moreText123"
    assert parse('<iframe src="https://www.youtube.com/embed/aBcDeFgHiJ"') == "https://youtu.be/aBcDeFgHiJ"
    assert parse('<iframe src="https://www.youtube.com/embed/invalid_characters!"') == "error"
    assert parse('<iframe src="https://www.youtube.com/watch?v=abc123"') == "error"
    # assert parse('<iframe src="https://vimeo.com/embed/abc123"') == "error"
    assert parse('<iframe src="https://www.youtube.com/"') == "error"
    assert parse('') == "error"


