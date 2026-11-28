from . import lexer, parser
from Graphing import grapher

def RunTerminal(message, shouldReturn):

    myLexer = lexer.Lexer() #cba to get better method
    myParser = parser.Parser()

    print(message)
    
    while True:
        uinput = input('> ')
        if uinput == 'M': #a menu call has been made, no point to even start lexing
            menuInput = input("You have entered the menu, type C to start calculating again, type G to enter graphing mode: ")
            if menuInput == 'C':
                continue
            elif menuInput == 'G': #the user has entered graphing mode
                grapher.create_y_vals()
        else:
            myLexer.ResetInitialise(uinput, 0)
            lexedTokens = myLexer.ParseText()
            myParser.ResetParser(lexedTokens)
            parsedResult = myParser.AddSub()
            if shouldReturn:
                return parsedResult
            
            print(parsedResult.value)