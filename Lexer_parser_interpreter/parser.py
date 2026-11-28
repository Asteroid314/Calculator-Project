from .errors import *
from .lexer import *
from Calculate.registry import execute

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
        
    def Peek(self):
        return self.tokensArray[self.idx + 1]
        
    def Factor(self):
        curr_token = self.token
        if curr_token.type == 'INT' and self.Peek().type != 'LPAREN':
            self.EatToken('INT')
                
        elif curr_token.type == 'FLT' and self.Peek().type != 'LPAREN':
            self.EatToken('FLT')
        
        elif (curr_token.type == 'NEGATE' or curr_token.type == 'LPAREN') or ((curr_token.type == 'INT' or curr_token.type == 'FLT') and self.Peek().type == 'LPAREN'): #one of two possibilities, -() or ()
            negative = False
            
            if curr_token.type == 'NEGATE':
                negative = True
                self.EatToken('NEGATE')
                
            if curr_token.type == 'INT':
                self.EatToken('INT')
                
            elif curr_token.type == 'FLT':
                self.EatToken('FLT')
            
            #there is a more efficient way to do this, but ultimately I can't be bothered to implement it.
            
            self.EatToken('LPAREN')
            result = self.AddSub()
            
            if negative:
                result.value = 0 - result.value #negating the value
                
            elif curr_token.type == 'INT' or curr_token.type == 'FLT':
                result.value = result.value * curr_token.value
                
            self.EatToken('RPAREN')
            
            if self.token.type == 'LPAREN':
                result.value = result.value * self.Factor().value
                
            return result
        else:
            raise InvalidExpressionError("The expression is invalid at index: ", self.idx)
        
        return curr_token

    def Power(self):
        leftToken = self.Factor()
        
        if self.token.type == 'FACT' and leftToken.type == 'INT':
            leftToken.value = execute("factorial", leftToken.value)
            self.EatToken('FACT')


        if self.token.type == 'POWER':
            self.EatToken('POWER')

            leftToken.value = execute("power", leftToken.value, self.Power().value)
            
        return leftToken

    def MulDiv(self):
        leftToken = self.Power()

        while self.token.type == 'MUL' or self.token.type == 'DIV':
            currentToken = self.token

            if currentToken.type == 'MUL':
                self.EatToken('MUL')
                leftToken.value = execute("multiply", leftToken.value, self.Power().value)

            elif currentToken.type == 'DIV':
                self.EatToken('DIV')
                leftToken.value = execute("divide", leftToken.value, self.Power().value)
                
            elif currentToken.type == 'MOD':
                self.EatToken('MOD')
                leftToken.value = execute("modulus", leftToken.value, self.Power().value)

        return leftToken

    def AddSub(self):
        leftToken = self.MulDiv()

        while self.token.type == 'PLUS' or self.token.type == 'MINUS':
            currentToken = self.token

            if currentToken.type == 'PLUS':
                self.EatToken('PLUS')
                leftToken.value = execute("add", leftToken.value, self.MulDiv().value)

            elif currentToken.type == 'MINUS':
                self.EatToken('MINUS')
                leftToken.value = execute("subtract", leftToken.value, self.MulDiv().value)

        return leftToken

    def ResetParser(self, newTokensArray):
        self.idx = 0
        self.tokensArray : list = newTokensArray
        self.token : Token = self.tokensArray[self.idx]