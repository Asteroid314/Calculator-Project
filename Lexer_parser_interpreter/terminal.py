from . import lexer, parser

def RunTerminal():

    myLexer = lexer.Lexer() #cba to get better method
    myParser = parser.Parser()

    print('Welcome to the C.L.I.V.E Calculator (Calculation Logic and Intelligent Value Engine)!')
    while True: #will change this
        uinput = input('> ')
        myLexer.ResetInitialise(uinput)
        lexedTokens = myLexer.ParseText()
        myParser.ResetParser(lexedTokens)
        parsedResult = myParser.AddSub()
        print(parsedResult.value)