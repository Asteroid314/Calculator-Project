from errors import *
import lexer

class Parser:
    def __init__(self):
        self.idx = 0
        self.tokensArray = None
        self.token = None

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

    def Factor(self):
        curr_token = self.token
        if curr_token.type == 'INT':
            self.EatToken('INT')
        elif curr_token.type == 'FLT':
            self.EatToken('FLT')
        else:
            raise InvalidExpressionError("The expression is invalid at index: ", self.idx)
        return curr_token

    def MulDiv(self):
        leftToken = self.Factor()

        while self.token.type == 'MUL' or self.token.type == 'DIV':
            currentToken = self.token

            if currentToken.type == 'MUL':
                self.EatToken('MUL')
                leftToken.value = leftToken.value * self.Factor().value

            elif currentToken.type == 'DIV':
                self.EatToken('DIV')
                leftToken.value = leftToken.value / self.Factor().value

        return leftToken

    def AddSub(self):
        leftToken = self.MulDiv()

        while self.token.type == 'PLUS' or self.token.type == 'MINUS':
            currentToken = self.token

            if currentToken.type == 'PLUS':
                self.EatToken('PLUS')
                leftToken.value = leftToken.value + self.MulDiv().value

            elif currentToken.type == 'MINUS':
                self.EatToken('MINUS')
                leftToken.value = leftToken.value - self.MulDiv().value

        return leftToken

    def ResetParser(self, newTokensArray):
        self.idx = 0
        self.tokensArray : list = newTokensArray
        self.token : lexer.Token = self.tokensArray[self.idx]