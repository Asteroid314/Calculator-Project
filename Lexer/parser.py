class Parser:
    def __init__(self, tokensArray):
        self.idx = 0
        self.tokensArray = tokensArray
        self.token = self.tokensArray[self.idx]

    def eatToken(self):
        self.idx += 1
        if self.idx < len(self.tokensArray):
            self.token = self.tokensArray[self.idx]
            return self.token
        return False

    def expr(self):
        