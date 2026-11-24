ARITHMETIC_OPERATORS = ['+', '-', '*', '/', '^', '!']
INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
BRACKETS = ['(', ')']
WHITELISTED = [' ']
FUNCTIONS = ['sin', 'cos', 'tan', 'sqrt']
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class InvalidParenthesisError(Exception):
    pass

class MissingTokenError(Exception):
    pass

class InvalidExpressionError(Exception):
    pass

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def getValue(self):
        return self.value

class Lexer:
    def __init__(self, expression):
        self.expression = self.SetExpression(expression)
        self.idx = 0
        self.char = self.expression[self.idx]
        self.currentNumberIndex = 0 #represents the index of the current number to be parsed, useful for multi character lexing

    def SetExpression(self, expr):
        if len(expr) == 0: #empty input
            raise InvalidExpressionError("Expression cannot be empty, please enter something")
        else:
            return expr

    def IncrementCharacter(self) -> bool: #increments the character along the string of tokens
        self.idx += 1
        self.currentNumberIndex += 1
        if self.idx < len(self.expression):
            self.char = self.expression[self.idx]
            return False
        else:
            return True

    def InterpretOperation(self) -> Token: #encodes an operation based on its type
        if self.char not in ARITHMETIC_OPERATORS and self.char not in BRACKETS:
            raise MissingTokenError("This character is not in the available syntax") #should not occur
        else:
            originalChar = self.char
            self.IncrementCharacter() #causes an incrementation so that the new character is the current
            if originalChar == '+':
                return Token('PLUS', '+')
            elif originalChar == '-':
                return Token('MINUS', '-')
            elif originalChar == '/':
                return Token('DIVIDE', '/')
            elif originalChar == '*':
                return Token('MULTIPLY', '*')
            elif originalChar == '^':
                return Token('POWER', '^')
            elif originalChar == '(':
                return Token('LPAREN', '(')
            elif originalChar == ')':
                return Token('RPAREN', ')')
            elif originalChar == '!':
                return Token('FACTORIAL', '!')

    def interpretFunction(self):
        self.currentNumberIndex = 0 #resetting current number index

        functionsTable = FUNCTIONS #creates a new copy of the functions table in order to filter out
        result = ''
        while (self.char in ALPHABET) and (self.idx < len(self.expression)):
            result += self.char
            self.IncrementCharacter()

        #this runs if a successful thing is found

        if result == 'sin':
            return Token('SIN', 'sin')
        elif result == 'cos':
            return Token('COS', 'cos')
        elif result == 'tan':
            return Token('TAN', 'tan')
        elif result == 'sqrt':
            return Token('SQRT', 'sqrt')
        else:
            raise InvalidExpressionError("Result not in functions")

    def InterpretNumber(self): #is able to encode integers and floating points
        floating = False
        result = ''

        while (self.char in INTEGERS or self.char == '.') and (self.idx < len(self.expression)):
            if self.char == '.': #checks for floating point symbol
                if not floating:
                    floating = True
                    result += self.char
                else:
                    raise InvalidExpressionError("This number has incorrect syntax: two floating points") #make more specific errors
            else:
                result += self.char

            self.IncrementCharacter()

        #after this has ran, the current char will be the one after the end of number
        
        if floating:
            return Token('FLT', float(result))
        else:
            return Token('INT', int(result))



    def ParseText(self): #iterates over tokens and checks for incorrect syntaxing
        resultantTokens = []
        eol = False #pointer to check the end of line
        balancedParenthesisCount = 0

        while self.idx < len(self.expression):

            while self.char in WHITELISTED:
                self.IncrementCharacter()
                if self.idx >= len(self.expression):
                    break

            if self.char in INTEGERS:
                resultantTokens.append(self.InterpretNumber())

            if self.char in ARITHMETIC_OPERATORS:
                resultantTokens.append(self.InterpretOperation())

            if self.char in ALPHABET:
                resultantTokens.append(self.interpretFunction())

            if self.char in BRACKETS:
                if self.char == '(':
                    balancedParenthesisCount += 1
                else:
                    balancedParenthesisCount -= 1

                if balancedParenthesisCount < 0: #caused by more than one right bracket without a left before it
                    raise InvalidParenthesisError("The parenthesis are ordered incorrectly.")
                resultantTokens.append(self.InterpretOperation())

            if self.char not in ARITHMETIC_OPERATORS and self.char not in INTEGERS and self.char not in BRACKETS and self.char not in WHITELISTED and self.char not in FUNCTIONS and self.char not in ALPHABET: #this should not occur, however there will be more debug added later
                raise InvalidExpressionError(f"This character is not in the available syntax: {self.char}")


        #this part of the lexer does simple debugging based on incorrect brackets
        if balancedParenthesisCount != 0:
            raise InvalidParenthesisError("The parenthesis do not cancel out")

        #add an EOL (End of line) token on the end of the lexed token output
        resultantTokens.append(Token('EOL:', '-1'))

        return resultantTokens