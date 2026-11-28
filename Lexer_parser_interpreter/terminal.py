from . import lexer, parser

def RunTerminal(message):

    myLexer = lexer.Lexer() #cba to get better method
    myParser = parser.Parser()

    print(message)
    while True: #will change this
        uinput = input('> ')
        myLexer.ResetInitialise(uinput)
        lexedTokens = myLexer.ParseText()
        myParser.ResetParser(lexedTokens)
        parsedResult = myParser.AddSub()
        return parsedResult