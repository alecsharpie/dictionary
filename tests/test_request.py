from dictionary.request import get_origin

def test_get_origin():
    assert type(get_origin('hello')) == str
