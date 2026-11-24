class Parser:
    def __init__(self, tokensArray):
        self.idx = 0
        self.tokensArray = tokensArray
        self.token = self.tokensArray[self.idx]

    def eatToken(self):
        pass

    def expr(self):
        pass