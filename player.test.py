from player import Player

player = Player('X')

def test_get_char():
    assert player.get_char() == 'X'

def test_get_token():
    assert player.get_token() == True

def test_set_tokenFalse():
    player.set_tokenFalse()
    assert player.get_token() == False

def test_player():
    test_get_char()
    test_get_token()
    test_set_tokenFalse()

test_player()