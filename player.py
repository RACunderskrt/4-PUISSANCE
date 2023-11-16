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
    
    def set_tokenTrue(self):
        self.token = True
    
    def verify_token_error(self, input):
        return len(input)>1 and (input[1] == 'R' or input[1] == 'r') and not self.get_token()