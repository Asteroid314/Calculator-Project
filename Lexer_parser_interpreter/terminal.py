from . import lexer, parser


def RunTerminal(message, shouldReturn):

    myLexer = lexer.Lexer() #cba to get better method
    myParser = parser.Parser()

    print(message)
    
    while True:
        uinput = input('> ')
        myLexer.ResetInitialise(uinput)
        lexedTokens = myLexer.ParseText()
        myParser.ResetParser(lexedTokens)
        parsedResult = myParser.AddSub()
        if shouldReturn:
            return parsedResult
        
        print(parsedResult.value)