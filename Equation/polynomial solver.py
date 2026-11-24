import math
def solvePolynomial(): #subprogram to select the degree of polynomial
    degree = input("Enter the degree of the polynomial")
    match degree:
        case 2:
            solveQuadratic()
            #some code to output it nicely and deal with repeated roots
            #some code that refrences an S/D or a format function to convert between surd, fraction and decimal
        case 3:
            solveCubic()
        case 4:
            solveQuartic()
        case 5:
            solveQuintic()
        case 6:
            solveSextic()
def solveQuadratic(): #solver for second degree polynomial
    a2 = input("Enter the coefficiant of the x^2 term: ") #takes the coefficiant of each term
    a1 = input("Enter the coeficiant of the x^1 term: ") #please find a better way to do this
    a0 = input("Enter the coefficiant of the x^0 term: ")
    try:#checks if the expression has real roots
        if ((a1)**2 - 4*(a2 * a0)) < 0:
            raise ValueError
        else:
            x1 = (-(a1)+math.sqrt((a1 ** 2) - 4*(a0 * a2)))/(2*a2)
            x2 = (-(a1)-math.sqrt((a1 ** 2) - 4*(a0 * a2)))/(2*a2)
            return[x1,x2]
    except ValueError:
        print("no real roots")
def solveCubic(): #Solves the cubics using the fromulae
    a3 = input("Enter the coefficiant of the x^3 term: ")
    a2 = input("Enter the coefficiant of the x^2 term: ") 
    a1 = input("Enter the coeficiant of the x^1 term: ") 
    a0 = input("Enter the coefficiant of the x^0 term: ")
    p = (3*a3*a1- a2**2)/ (3 * a3**2) #used to find discriminant in depressed cubic form or smth
    q = (2 * a2 ** 3 - 9 *a3 * a2 * a1 + 27 * a3**2 * a0)/ (27 * a3**3)
    discriminant = -(4*(p**3))-(27*(q**2))
    if discriminant < 0: #checks which method to use
        #Cardano's formula
        return [-1,-1,-1] # placeholder
    elif discriminant == 0:
        if p == 0 and q == 0:
            return [-(a2/ (3 * a3)),-(a2/ (3 * a3)),-(a2/ (3 * a3))]
        else:
            return [(3*q)/(2*p),(3*q)/(2*p), -((3*q)/p)]
    elif discriminant > 0:
        #use Cardano's formula casus irreduciblis 
        return[-1,-1,-1]
def solveQuartic(): #method to solve quartics
    a4 = input("Enter the coefficiant of the x^4 term: ")
    a3 = input("Enter the coefficiant of the x^3 term: ")
    a2 = input("Enter the coefficiant of the x^2 term: ") 
    a1 = input("Enter the coeficiant of the x^1 term: ") 
    a0 = input("Enter the coefficiant of the x^0 term: ")
    #it's late this is complicated the maths is too hard will look at it another time
    return [-1,-1,-1,-1] # placeholder for output format
def solveQuintic(): #method to solve quintics
    a5 = input("Enter the coefficiant of the x^5 term: ")
    a4 = input("Enter the coefficiant of the x^4 term: ")
    a3 = input("Enter the coefficiant of the x^3 term: ")
    a2 = input("Enter the coefficiant of the x^2 term: ") 
    a1 = input("Enter the coeficiant of the x^1 term: ") 
    a0 = input("Enter the coefficiant of the x^0 term: ")
    #use a solve N adjacent method as no fromula
    #iteate from -1000 to 1000 with some decimal places and check if its zero to those decimal places
    #if never = 0 then no real roots
    return[-1,-1,-1,-1,-1] # placeholder for output forat
def solveSextic(): #A method to solve sextics
    a6 = input("Enter the coefficiant of the x^6 term: ")
    a5 = input("Enter the coefficiant of the x^5 term: ")
    a4 = input("Enter the coefficiant of the x^4 term: ")
    a3 = input("Enter the coefficiant of the x^3 term: ")
    a2 = input("Enter the coefficiant of the x^2 term: ") 
    a1 = input("Enter the coeficiant of the x^1 term: ") 
    a0 = input("Enter the coefficiant of the x^0 term: ")
    #exactly the same as a quintic but have x^6 term
    return [-1,-1,-1,-1,-1,-1] #placeholder for output format
