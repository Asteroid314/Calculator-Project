
# Constants
PI = 3.141592653589793238462643
ARCTANS = [0.7853981633974483, 0.4636476090008061, 
           0.2449786631268641, 0.1243549945467614, 
           0.0624188099959574, 0.0312398334302683, 
           0.0156237286204768, 0.0078123410601011, 
           0.0039062301319670, 0.0019531225164788, 
           0.0009765621895593, 0.0004882812111949, 
           0.0002441406201494, 0.0001220703118937, 
           0.0000610351561742, 0.0000305175781155, 
           0.0000152587890613, 0.0000076293945311, 
           0.0000038146972656, 0.0000019073486328, 
           0.0000009536743164, 0.0000004768371582, 
           0.0000002384185791, 0.0000001192092896, 
           0.0000000596046448, 0.0000000298023224, 
           0.0000000149011612, 0.0000000074505806]
K = 0.6072529350088813

# When the type of multiple variables could cause the same error, use this to specify the value
class VariableTypeError(TypeError):
    def __init__(self, value):
        self.value = value
        super().__init__()

# When the value of multiple variables could cause the same error, use this to specify the value
class VariableValueError(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__()


class Operation:
    def __init__(self, name, operands):
        self.operands = operands
        self.name = name

    # Selects the input operation
    def selectOp(self):
        try:
            match self.name:
                case "add": return self.add()
                case "sub": return self.sub()
                case "mult": return self.mult()
                case "div": return self.div()
                case "pow": return self.pow()
                case "ceil": return self.ceil()
                case "abs": return self.abs()
                case "floor": return self.floor()
                case "sin": return self.sin()
                case "cos": return self.cos()
                case "tan": return self.tan()
                case "fact": return self.fact()
                case "sqrt": return self.sqrt()
                case "choose": return self.choose()
                case _: raise ValueError
        except ValueError:
            print(f"Operation {self.name} is invalid.")

    # Performs the selected operation on the input operands
    def performOp(self):
        return self.selectOp()

    # Calculates the sum of x and y
    def add(self):
        x = self.operands[0]
        y = self.operands[1]
        try:
            if type(x) != int and type(x) != float:
                raise VariableTypeError(x)
            elif type(y) != int and type(y) != float:
                raise VariableTypeError(y)
            else:
                return x + y
        except VariableTypeError as e:
            print("Cannot perform operation 'add' on non-numeric value {e.value}.")

    # Calculates the difference of x and y
    def sub(self):
        x = self.operands[0]
        y = self.operands[1]
        try:
            if type(x) != int and type(x) != float:
                raise VariableTypeError(x)
            elif type(y) != int and type(y) != float:
                raise VariableTypeError(y)
            else:
                return x - y
        except VariableTypeError as e:
            print("Cannot perform operation 'sub' on non-numeric value {e.value}.")

    # Calculates the product of x and y
    def mult(self):
        x = self.operands[0]
        y = self.operands[1]
        try:
            if type(x) != int and type(x) != float:
                raise VariableTypeError(x)
            elif type(y) != int and type(y) != float:
                raise VariableTypeError(y)
            else:
                return x * y
        except VariableTypeError as e:
            print("Cannot perform operation 'mult' on non-numeric value {e.value}.")

    # Calculates the quotient of x and y
    def div(self):
        x = self.operands[0]
        y = self.operands[1]
        try:
            if type(x) != int and type(x) != float:
                raise VariableTypeError(x)
            elif type(y) != int and type(y) != float:
                raise VariableTypeError(y)
            elif x == 0 and y == 0:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            else:
                return x / y
        except VariableTypeError as e:
            print(f"Cannot perform operation 'div' on non-numeric value {e.value}.")
        except ValueError:
            print("Operation 'div' (x/y) is indeterminate at x=0, y=0.")
        except ZeroDivisionError:
            print(f"Operation 'div' (x/y) is undefined at y={y}.")

    # Calculates the result of raising x to the yth power
    def pow(self):
        x = self.operands[0]
        y = self.operands[1]
        try:
            if type(x) != int and type(x) != float:
                raise VariableTypeError(x)
            elif type(y) != int and type(y) != float:
                raise VariableTypeError(y)
            elif x == y == 0:
                raise ValueError
            else:
                return x ** y
        except VariableTypeError as e:
            print(f"Cannot perform operation 'pow' on non-numeric value {e.value}.")
        except ValueError:
            print("Operation 'pow' (x^y) is undefined at x=0, y=0.")

    
    # Calculates the least integer greater than or equal to x
    def ceil(self):
        x = self.operands[0]
        try:
            if type(x) != int and type(x) != float:
                raise TypeError
            else:
                int_x = int(x)
                if x > int_x:
                    return int_x + 1
                return int_x
        except TypeError:
            print(f"Cannot perform operation 'ceil' on non-numeric value {x}.")

    # Calculates the magnitude of x
    def abs(self):
        x = self.operands[0]
        try:
            if type(x) != int and type(x) != float:
                raise TypeError
            else:
                if x < 0:
                    return -x
                return x
        except TypeError:
            print(f"Cannot perform operation 'abs' on non-numeric value {x}.")

    # Calculates the greatest integer less than or equal to x
    def floor(self):
        x = self.operands[0]
        try:
            if type(x) != int and type(x) != float:
                raise TypeError
            else:
                int_x = int(x)
                if x < int_x:
                    return int_x - 1
                return int_x
        except TypeError:
            print(f"Cannot perform operation 'floor' on non-numeric value {x}.")

    # Calculates sine and cosine of x radians.
    def _cordic(self):
        z = self.operands[0]
        # Wrap any input angle into one full period [0, 2pi]
        z %= 2 * PI

        # Wrap angle into [-pi, +pi]
        if z > PI:
            z -= 2 * PI
        elif z < -PI:
            z += 2 * PI

        # Pre-rotate into [-pi/2, +pi/2] and initialise.
        if z > PI / 2:
            x, y = 0, K
            z -= PI / 2
        elif z < -PI / 2:
            x, y = 0, -K
            z += PI / 2
        else:
            x, y = K, 0

        # Main loop - converge on exact angle
        for i in range(55):
            step = ARCTANS[i] if i < len(ARCTANS) else (2 ** -i)
            if z >= 0:
                xNext, yNext, zNext = x - (y * (2 ** -i)), y + (x * (2 ** -i)), z - step
            else:
                xNext, yNext, zNext = x + (y * (2 ** -i)), y - (x * (2 ** -i)), z + step
            x, y, z = xNext, yNext, zNext
        return round(x, 14) + 0.0, round(y, 14) + 0.0

    # Calculates the sine of x radians
    def sin(self):
        z = self.operands[0]
        print(z, type(z))
        try:
            if type(z) != int and type(z) != float:
                print(type(z))
                raise TypeError
            else:
                return self._cordic()[1]
        except TypeError:
            print(f"Cannot perform operation 'sin' on non-numeric value {z}.")

    # Calculates the cosine of x radians
    def cos(self):
        z = self.operands[0]
        try:
            if type(z) != int and type(z) != float:
                raise TypeError
            else:
                return self._cordic()[0]
        except TypeError:
            print(f"Cannot perform operation 'cos' on non-numeric value {z}.")

    # Calculates the tangent of x radians
    def tan(self):
        z = self.operands[0]
        cordicResult = self._cordic()
        try:
            if type(z) != int and type(z) != float:
                raise TypeError
            elif cordicResult[0] == 0:
                raise ValueError
            else:
                return cordicResult[1] / cordicResult[0]
        except TypeError:
            print(f"Cannot perform operation 'tan' on non-numeric value {z}.")
        except ValueError:
            print(f"Operation 'tan' is undefined at {z} radians.")

    # Calculates the factorial of a non-negative integer
    def fact(self):
        n = self.operands[0]
        try:
            if type(n) != int:
                raise TypeError
            if n < 0:
                raise ValueError
            else:
                result = 1
                for i in range(2, n + 1):
                    result *= i
                return result
        except TypeError:
            print(f"Cannot perform operation 'fact' on non-integer value {n}.")
        except ValueError:
            print(f"Operation 'fact' is undefined at {n}.")

    # Calculates the principal square root of a positive number s
    def sqrt(self):
        s = self.operands[0]
        try:
            if type(s) != int and type(s) != float:
                raise TypeError
            elif s < 0:
                raise ValueError
            else:
                xNext = 0.1
                x = s
                while xNext != x:
                    x = xNext
                    xNext = (x + s / x) / 2
                return xNext
        except TypeError:
            print(f"Cannot perform operation 'sqrt' on non-numeric value {s}.")
        except ValueError:
            print(f"Cannot perform operation 'sqrt' on negative number {s}.")

    # Calculates the number of combinations
    def choose(self):
        n = self.operands[0]
        r = self.operands[1]
        try:
            if type(n) != int:
                raise VariableTypeError(n)
            elif type(r) != int:
                raise VariableTypeError(r)
            elif n < 0:
                raise VariableValueError(n)
            elif r < 0:
                raise VariableValueError(r)
            elif r > n:
                raise ValueError
            else:
                r = min(r, n - r)
                result = 1
                for i in range(1, r + 1):
                    result = (result * (n - i + 1)) // i
                return result
        except VariableTypeError as e:
            print(f"Cannot perform operation 'choose' on non-integer {e.value}.")
        except VariableValueError as e:
            print(f"Cannot perform operation 'choose' on negative number {e.value}.")
        except ValueError:
            print(f"Operation 'choose' (nCr) is undefined at n = {n}, r = {r} (r>n).")
        
