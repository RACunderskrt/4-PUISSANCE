import copy

from player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.grid = [[None for i in range(6)] for j in range(7)]
        self.grid_horizontal = [[None for i in range(7)] for j in range(6)]
        self.grid_diagonal_left = []
        self.grid_diagonal_right = []
        grid_diagonal_left = [[None for _ in range(i)] for i in range(4,7)]
        self.grid_diagonal_left = copy.deepcopy(grid_diagonal_left) + copy.deepcopy(grid_diagonal_left[::-1])
        self.grid_diagonal_right = copy.deepcopy(self.grid_diagonal_left)

    def get_grid(self):
        return self.grid
    
    def get_player1(self):
        return self.player1
    
    def get_player2(self):
        return self.player2
    
    def get_grid_horizontal(self):
        return self.grid_horizontal
    
    def set_grid(self, grid):
        self.grid = grid

    def columnFull(self, column):
        return self.grid[column].count(None) <= 0
    
    def insert(self, column, player):
        if(self.columnFull(column)):
            raise Exception("Column ", str(column), " is full")
        x = self.grid[column].index(None)
        self.grid[column][x] = player.get_char()
        self.grid_horizontal[x][column] = player.get_char()
        index_left = column + x - 3
        index_right = x - column + 3
        if 0 <= index_left < 6:
            self.grid_diagonal_left[index_left][x if index_left < 4 else 6-column] = player.get_char()
        if 0 <= index_right < 6:
            self.grid_diagonal_right[index_right][x if index_right < 4 else column] = player.get_char()

    def verify_all(self):
        return self.verify(self.grid_horizontal) or self.verify(self.grid) or self.verify(self.grid_diagonal_left) or self.verify(self.grid_diagonal_right)
    
    def grid_full(self):
        return not any(None in column for column in self.grid)

    def verify(self, arr):
        for next_arr in arr:
            counter = 0
            test_value = next_arr[0]
            for next_value in next_arr: 
                if(next_value == test_value):
                    counter += 1
                else:
                    counter = 1
                    test_value = next_value            
                if(counter >= 4):
                    if(test_value == None):
                        continue
                    return True
        return False
    
    def reverse(self, column):
        x = self.grid[column].index(None)       
        bufArr = self.grid[column][0:x]
        self.grid[column][0:x] = bufArr[::-1]