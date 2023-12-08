from game import Game
from player import Player

P1 = Player("Thomas", "A")
P2 = Player("Alexandre", "B")
TEST_VALUE = Game()

def test_get_grid():
    test_arr = [[None for i in range(6)] for j in range(7)]
    assert TEST_VALUE.get_grid() == test_arr

def test_get_player1():
    assert TEST_VALUE.get_player1().get_name() == P1.get_name()

def test_get_player2():
    assert TEST_VALUE.get_player2().get_id() == P2.get_id()

def test_insert_vertical():
    TEST_VALUE.insert(1,P1)
    TEST_VALUE.insert(1,P1)
    bufGrid = [[None for _ in range(6)],
               [P1,P1,None,None,None,None],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)]]
    assert TEST_VALUE.get_grid() == bufGrid

def test_insert_horizontal():
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(2,P1)
    bufGrid = [[P1,None,P1,None,None,None, None],
               [None for _ in range(7)],
               [None for _ in range(7)],
               [None for _ in range(7)],
               [None for _ in range(7)],
               [None for _ in range(7)]]
    assert TEST_VALUE.get_grid_horizontal() == bufGrid

def test_check():
    test_arr = [[None,None,None,None,1,1,1,1]]
    test_arr1 = [[None,None,None,1,None,1,1,1]]
    assert TEST_VALUE.check(test_arr)[0] and not TEST_VALUE.check(test_arr1)[0]

def reset_grid():
    TEST_VALUE.reset_grid()

def test_reverse_vertical():
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(0,P2)
    TEST_VALUE.reverse(0)
    bufGrid = [[P2,P1,P1,None,None,None],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)],
               [None for _ in range(6)]]
    assert TEST_VALUE.get_grid() == bufGrid

def test_reverse_horizontal():
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(0,P2)
    TEST_VALUE.reverse(0)
    bufGrid = [[P2, None, None, None, None, None, None],
               [P1, None, None, None, None, None, None],
               [P1, None, None, None, None, None, None],
               [None for _ in range(7)],
               [None for _ in range(7)],
               [None for _ in range(7)]]
    assert TEST_VALUE.get_grid_horizontal() == bufGrid

def test_reverse_diagonal_left():
    TEST_VALUE.insert(4,P1)
    TEST_VALUE.insert(4,P1)
    TEST_VALUE.insert(4,P2)
    TEST_VALUE.reverse(0)
    bufGrid = [[None, None, None, None],
               [P1, None, None, None, None],
               [None, P1, None, None, None, None],
               [None, None, P2, None, None, None],
               [None, None, None, None, None],
               [None, None, None, None]]
    assert TEST_VALUE.get_grid_diagonal()[0] == bufGrid

def test_reverse_diagonal_right():
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(0,P1)
    TEST_VALUE.insert(0,P2)
    TEST_VALUE.reverse(0)
    bufGrid = [[None, None, None, None],
               [None, None, None, None, None],
               [None, None, None, None, None, None],
               [P2, None, None, None, None, None],
               [P1, None, None, None, None],
               [P1, None, None, None]]
    assert TEST_VALUE.get_grid_diagonal()[1] == bufGrid

def test_column_full():
    for _ in range(6):
        TEST_VALUE.insert(0,P1)
    assert TEST_VALUE.columnFull(0) 

def test_grid_full():
    for i in range(7):   
        for _ in range(6):
            TEST_VALUE.insert(i,P1)
    assert TEST_VALUE.gridFull()


def test_game():
    test_get_grid()
    test_get_player1()
    test_get_player2()
    test_insert_vertical()
    reset_grid()
    test_insert_horizontal()
    reset_grid()
    test_check()
    test_reverse_vertical()
    reset_grid()
    test_reverse_horizontal()
    reset_grid()
    test_reverse_diagonal_left()
    reset_grid()
    test_reverse_diagonal_right()
    reset_grid()
    test_grid_full()
    reset_grid()
    test_column_full()

test_game()