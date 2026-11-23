
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

# Calculates the least integer greater than or equal to x
def ceil(x):
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

# Calculates the greatest integer less than or equal to x
def floor(x):
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

# Calculates the magnitude of x
def abs(x):
    try:
        if type(x) != int and type(x) != float:
            raise TypeError
        else:
            if x < 0:
                return -x
            return x
    except TypeError:
        print(f"Cannot perform operation 'abs' on non-numeric value {x}.")

# Calculates sine and cosine of x radians.
def _cordic(z):
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

def sin(z):
    try:
        if type(z) != int and type(z) != float:
            raise TypeError
        else:
            return _cordic(z)[1]
    except TypeError:
        print(f"Cannot perform operation 'sin' on non-numeric value {z}.")

def cos(z):
    try:
        if type(z) != int and type(z) != float:
            raise TypeError
        else:
            return _cordic(z)[0]
    except TypeError:
        print(f"Cannot perform operation 'cos' on non-numeric value {z}.")

def tan(z):
    cordicResult = _cordic(z)
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

# Calculates the product of integers 1 to x
def factorial(x): 
    try:
        if type(x) != int:
            raise TypeError
        elif x < 0:
            raise ValueError
        else:
            result = 1
            for i in range(1, x+1):
                result *= i
            return result
    except ValueError:
        print(f"Cannot perform operation 'factorial' on negative number {x}.")
    except TypeError:
        print(f"Cannot perform operation 'factorial' on non-integer {x}.")

# Calculates the principal square root of a positive number s
def sqrt(s):
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