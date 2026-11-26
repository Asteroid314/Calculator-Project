class Operation:
    def __init__(self, name, operands):
        self.operands = operands
        self.name = name

    # Selects the input operation
    def select_op(self):
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
                case "arcsin": return self.arcsin()
                case "fact": return self.fact()
                case "sqrt": return self.sqrt()
                case "cbrt": return self.cbrt()
                case "nroot": return self.nroot()
                case "choose": return self.choose()
                case _: raise ValueError
        except ValueError:
            print(f"Operation '{self.name}' is invalid.")

    # Performs the selected operation on the input operands
    def perform_op(self):
        return self.select_op()
    
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

    # Calculates the principal square root of a positive number s
    def sqrt(self):
        s = self.operands[0]
        try:
            if type(s) != int and type(s) != float:
                raise TypeError
            elif s < 0:
                raise ValueError
            else:
                xNext = 0.1 if s != 0.1 else 0.2
                x = s
                while xNext != x:
                    x = xNext
                    xNext = (x + s / x) / 2
                return xNext
        except TypeError:
            print(f"Cannot perform operation 'sqrt' on non-numeric value {s}.")
        except ValueError:
            print(f"Cannot perform operation 'sqrt' on negative number {s}.")

    def cbrt(self):
        c = self.operands[0]
        try:
            if type(c) != int and type(c) != float:
                raise TypeError
            else:
                xNext = 0.1 if c != 0.1 else 0.2
                x = c
                while xNext != x:
                    x = xNext
                    xNext = ((c / (x ** 2)) + (2 * x)) / 3
                return xNext
        except TypeError:
            print(f"Cannot perform operation 'cbrt' on non-numeric value {c}.")

    def nroot(self):
        n = self.operands[0] # Index (the nth root is taken)
        p = self.operands[1] # Radicand (the root of p is taken)
        try:
            if type(n) != int and type(n) != float:
                raise VariableTypeError(n)
            elif type(p) != int and type(p) != float:
                raise VariableTypeError(p)
            elif type(n) != int:
                raise NotImplementedError
            elif n == 0 or (n % 2 == 0 and p < 0):
                raise ValueError
            else:
                xNext = 0.1 if p != 0.1 else 0.2
                x = p
                while xNext != x:
                    x = xNext
                    xNext = ((p / (x ** (n - 1))) + (x * (n - 1))) / n
                return xNext
        except VariableTypeError as e:
            print(f"Cannot perform operation 'nroot' on non-numeric value {e.value}.")
        except NotImplementedError:
            print("Non-integer roots have not yet been implemented.")
        except ValueError:
            if n == 0:
                print("Operation 'nroot' (p^(1/n)) is undefined at n=0.")
            else:
                print(f"Operation 'nroot' (p^(1/n)) is undefined for negative p with even n.")
            

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