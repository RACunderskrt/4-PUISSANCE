from player import Player

PLAYER = Player('X', 1)

def test_get_name():
    assert PLAYER.get_name() == 'X'

def test_get_id():
    assert PLAYER.get_id() == 1

def test_get_token():
    assert PLAYER.get_token() == True

def test_set_tokenFalse():
    PLAYER.set_tokenFalse()
    assert PLAYER.get_token() == False

def test_verify_token_error_true(): #the token is valid
    PLAYER.set_tokenFalse()
    assert PLAYER.verifyToken("5R")

def test_verify_token_error_false(): #the token is invalid
    assert not PLAYER.verifyToken("5R")




def test_player():
    test_get_name()
    test_get_token()
    test_set_tokenFalse()
    PLAYER.set_tokenTrue()
    test_verify_token_error_true()
    PLAYER.set_tokenTrue()
    test_verify_token_error_false()


test_player()