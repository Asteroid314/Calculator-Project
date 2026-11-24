from Calculate.operations import Operation, VariableValueError, VariableTypeError

class InvalidPolynomialError(ValueError):
    pass

class PolynomialSolver:
    def __init__(self, degree, coefficients):
        self.degree = degree # Largest power of x that occurs in the polynomial
        self.coefficients = coefficients # Assume coefficients are ordered a_0, a_1, a_2, etc. (ascending powers of x)

    # Selects the input degree of polynomial equation
    def selectDegree(self):
        d = self.degree
        try:
            if type(d) != int:
                raise TypeError
            elif d <= 0:
                raise ValueError
            elif d > 6:
                raise NotImplementedError
            else:
                match d:
                    case 1: return self.solveLinear()
                    case 2: return self.solveQuadratic()
                    case 3: return self.solveCubic()
                    case 4: return self.solveQuartic()
                    case 5: return self.solveQuintic()
                    case 6: return self.solveSextic()
                    case _: print("Someone's a silly AI!")
        except TypeError:
            print(f"A polynomial cannot have non-integer degree {d}.")
        except ValueError:
            if d == 0:
                print(f"A degree-0 polynomial equation has no solutions.")
            elif d < 0:
                print(f"A polynomial cannot have negative degree {d}.")
            else:
                print("This should not happen.")
        except NotImplementedError:
            print(f"Solution of polynomials of degree {d} has not yet been implemented.")

    # Solves the selected degree of polynomial equation
    def solvePolynomial(self):
        return self.selectDegree()

    # Checks whether the polynomial to be solved is or is not valid
    def validatePolynomial(self):
        c = self.coefficients
        d = self.degree
        try:
            for a in c:
                if type(a) != int and type(a) != float: # All coefficients must be numeric
                    raise VariableTypeError(a, c.index(a))
            if c[d] == 0: # Leading coefficient cannot equal 0 (this would effectively change the degree of the polynomial)
                raise ZeroDivisionError
            return True
        except VariableTypeError as e:
            print(f"Coefficient of term in x^{e.index} in polynomial cannot have non-numeric value {e.value}.")
            return False
        except ZeroDivisionError:
            print(f"Leading coefficient of polynomial cannot equal 0.")
            return False

    # Solves polynomial equations of degree 1
    def solveLinear(self):
        a = self.coefficients
        try:
            if not self.validatePolynomial():
                raise InvalidPolynomialError
            else:
                return [(- a[0]) / a[1]]
        except InvalidPolynomialError:
            print("Cannot solve polynomial due to validation failing (see specific error above).")

    # Solves polynomial equations of degree 2
    def solveQuadratic(self):
        a = self.coefficients
        try:
            if not self.validatePolynomial():
                raise InvalidPolynomialError
            discriminant = (a[1] ** 2) - (4 * a[2] * a[0])
            if discriminant < 0: # No real roots
                raise ValueError
            elif discriminant == 0: # Repeated root - kept to maintain multiplicity
                root0 = (- a[1]) / (2 * a[2])
                return [root0, root0]
            else:
                sqrt = Operation("sqrt", [discriminant])
                sqrtResult = sqrt.performOp()
                root0 = (- a[1] + sqrtResult) / (2 * a[2])
                root1 = (- a[1] - sqrtResult) / (2 * a[2])
                return [root0, root1]
        except InvalidPolynomialError:
            print("Cannot solve polynomial due to validation failing (see specific error above).")
        except ValueError:
            print(f"Polynomial '{a[0]} + {a[1]}x + {a[2]}x^2' has no real roots.")

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
