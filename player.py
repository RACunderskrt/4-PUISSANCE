import re

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.token = True
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_token(self):
        return self.token
    
    def set_tokenFalse(self):
        self.token = False

    def set_tokenTrue(self):
        self.token = True

    def verifyToken(self, input):
        return len(input) > 1 and re.search("[rR]",input[1]) and not self.get_token()