from game import Game
from player import Player

P1 = Player('A')
P2 = Player('B')
TEST_VALUE = Game(P1,P2)

def test_get_grid():
    test_arr = [[None for i in range(6)] for j in range(7)]
    assert TEST_VALUE.get_grid() == test_arr

def test_get_player1():
    assert TEST_VALUE.get_player1() == P1

def test_get_player2():
    assert TEST_VALUE.get_player2() == P2

def test_insert_vertical():
    TEST_VALUE.insert(1,P1)
    TEST_VALUE.insert(1,P1)
    bufGrid = [[None for i in range(6)],['A','A',None,None,None,None],[None for i in range(6)],[None for i in range(6)],[None for i in range(6)],[None for i in range(6)],[None for i in range(6)]]
    assert TEST_VALUE.get_grid() == bufGrid

def test_insert_horizontal():
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(2,P1)
    bufGrid = [['A',None,None,None,None,None],[None for i in range(6)],['A',None,None,None,None,None],[None for i in range(6)],[None for i in range(6)],[None for i in range(6)],[None for i in range(6)]]
    assert TEST_VALUE.get_grid() == bufGrid

def test_verify():
    test_arr = [[None,None,None,None,1,1,1,1]]
    test_arr1 = [[None,None,None,1,None,1,1,1]]
    assert TEST_VALUE.verify(test_arr) and not TEST_VALUE.verify(test_arr1)

def reset_grid():
    TEST_VALUE.set_grid([[None for i in range(6)] for j in range(7)])

def test_reverse():
    test_arr = [[1,2,3,None,None,None]]
    bufGrid = [[3,2,1,None,None,None]]
    TEST_VALUE.set_grid(test_arr)
    TEST_VALUE.reverse(0)
    assert TEST_VALUE.get_grid() == bufGrid


def test_game():
    test_get_grid()
    test_get_player1()
    test_get_player2()
    test_insert_vertical()
    reset_grid()
    test_insert_horizontal()
    reset_grid()
    test_verify()
    test_reverse()
    reset_grid()

test_game()