class Player:
    def __init__(self, char):
        self.char = char
        self.token = True

    def get_char(self):
        return self.char
    
    def get_token(self):
        return self.token
    
    def set_tokenFalse(self):
        self.token = False