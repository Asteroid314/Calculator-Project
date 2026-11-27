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