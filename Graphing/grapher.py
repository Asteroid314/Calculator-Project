from Lexer_parser_interpreter import lexer
from Lexer_parser_interpreter import parser

def create_y_vals():
    expression = input("Please enter the equation you would like to graph, using 'X' as the variable: ")
    upperRange, lowerRange = int(input("Please state the upper X value, inclusive: ")), int(input("Please state the lower X value, inclusive: "))
    
    graphLexer = lexer.Lexer()
    graphParser = parser.Parser()
    
    for xVal in range(lowerRange, upperRange+1):
        graphLexer.ResetInitialise(expression, xVal)
        lexedText = graphLexer.ParseText()
        graphParser.ResetParser(lexedText)
        res = graphParser.AddSub()
        print(res.value)
