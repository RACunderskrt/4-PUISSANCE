class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.grid = [[0 for i in range(6)] for j in range(7)]
        self.grid_horizontal = [[0 for i in range(7)] for j in range(6)]
        self.grid_diagonal_left

    def get_grid(self):
        return self.grid
    
    def get_player1(self):
        return self.player1
    
    def get_player2(self):
        return self.player2
    
    def set_grid(self, grid):
        self.grid = grid


 
