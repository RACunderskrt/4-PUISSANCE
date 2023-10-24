from player import Player

PLAYER = Player('X')

def test_get_char():
    assert PLAYER.get_char() == 'X'

def test_get_token():
    assert PLAYER.get_token() == True

def test_set_tokenFalse():
    PLAYER.set_tokenFalse()
    assert PLAYER.get_token() == False

def test_player():
    test_get_char()
    test_get_token()
    test_set_tokenFalse()

test_player()