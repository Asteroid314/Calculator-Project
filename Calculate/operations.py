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
    def absolute(self):
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