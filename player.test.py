from player import Player

PLAYER = Player('X')

def test_get_char():
    assert PLAYER.get_char() == 'X'

def test_get_token():
    assert PLAYER.get_token() == True

def test_set_tokenFalse():
    PLAYER.set_tokenFalse()
    assert PLAYER.get_token() == False

def test_verify_token_error_true():
    PLAYER.set_tokenFalse()
    assert PLAYER.verify_token_error("5R") == True

def test_verify_token_error_false():
    assert PLAYER.verify_token_error("5") == False and PLAYER.verify_token_error("5R")

def test_verify_token_error_false():
    assert PLAYER.verify_token_error("5R") == False



def test_player():
    test_get_char()
    test_get_token()
    test_set_tokenFalse()
    PLAYER.set_tokenTrue()
    test_verify_token_error_true()
    PLAYER.set_tokenTrue()
    test_verify_token_error_false()


test_player()