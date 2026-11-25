from errors import *
import lexer

class Parser:
    def __init__(self, tokensArray):
        self.idx = 0
        self.tokensArray = tokensArray
        self.token : lexer.Token = self.tokensArray[self.idx]

    def IncrementCharacter(self):
        self.idx += 1
        if self.idx < len(self.tokensArray):
            self.token = self.tokensArray[self.idx]
            return self.token
        return False

    def EatToken(self, tokenType):
        if self.token.type == tokenType: #therefore it is correct
            self.IncrementCharacter()
        else:
            raise EatingTokenError("The token type you are inputting does not match the current token type")

    def factor(self):
        curr_token = self.token
        if curr_token.type == 'INT' or curr_token.type == 'FLT':
            self.EatToken()
            return self.token

    def term(self):
        node = self.factor()

        while self.token.type == 'MUL' or self.token.type == 'DIV':
            currentToken = self.token

            if currentToken.type == 'MUL':
                self.eatToken()
            