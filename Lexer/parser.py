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

    def Factor(self):
        curr_token = self.token
        if curr_token.type == 'INT':
            self.EatToken('INT')
        elif curr_token.type == 'FLT':
            self.EatToken('FLT')
        else:
            raise InvalidExpressionError("The expression is invalid at index: ", self.idx)
        return self.token

    def MulDiv(self):
        leftToken = self.factor()

        while self.token.type == 'MUL' or self.token.type == 'DIV':
            currentToken = self.token

            if currentToken.type == 'MUL':
                self.eatToken('MUL')
                result = result * self.Factor()

            elif currentToken.type == 'DIV':
                self.EatToken('DIV')
                result = result / self.Factor()

    def AddSub(self):

        leftToken = self.MulDiv()

        while self.token.type == 'PLUS' or self.token.type == 'MINUS':
            currentToken = self.token

            if currentToken.type == 'PLUS':
                self.EatToken('PLUS')
                result = result + self.MulDiv()

            elif currentToken.type == 'MINUS':
                self.EatToken('MINUS')
                result = result - self.MulDiv()


    def BracketsIndicies(self):

        leftToken
            