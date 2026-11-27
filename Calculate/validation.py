from .exceptions import VariableValueError, VariableTypeError
from .constants import *

def ensure_range(min, max, min_inclusive : bool, max_inclusive : bool, *operands) -> tuple:
    """Return all operands if they fall into the required range.
    Else raise ValueError."""
    for operand in operands:
        if min_inclusive and operand < min:
            raise ValueError(f"All operands must be greater than or equal to {min}.")
        elif operand <= min:
            raise ValueError(f"All operands must be greater than {min}.")
        elif max_inclusive and operand > max:
            raise ValueError(f"All operands must be less than or equal to {max}.")
        elif operand >= max:
            raise ValueError(f"All operands must be less than {max}.")
    return operands

def ensure_not_all(val, *operands):
    """Return all values if not all equal to val.
    Else raise ValueError"""
    for i in range(len(operands)):
        operand = operands[i]
        if operand != val:
            return operands
    raise ValueError(f"Not all operands can equal {val}.")

def ensure_domain(value, max):
    """Ensure value is less than or equal to max in magnitude."""
    if abs(value) > max:
        raise ValueError(
            f"Domain error: |x| must be <= {max} (currently {value})."
        )
    return value

def check_real(x, name="x", allow_inf=False):
    """Return x unchanged if it is a valid real number, else raise.
       
    TypeError  : not an int or float (bool rejected on purpose).
    ValueError : NaN, or an infinity when allow_inf is False.
    """
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a real number, got {type(x).__name__}")
    if isinstance(x, float):
        if x != x:
            raise ValueError(f"{name} must not be NaN")
        if not allow_inf and (x == INF or x == -INF):
            raise ValueError(f"{name} must be finite")
    return x

def validate_nth_root(s, n):
    """Return (s, n) as floats, or raise TypeError / ValueError."""
    for name, v in (("s", s), ("n", n)):
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError(f"{name} must be a real number, got {type(v).__name__}")
    try:
        s, n = float(s), float(n)
    except OverflowError:
        raise ValueError("s and n must be representable as finite floats") from None

    if s != s or n != n:
        raise ValueError("s and n must not be NaN")
    if s == INF or s == -INF or n == INF or n == -INF:
        raise ValueError("s and n must be finite")
    if n == 0.0:
        raise ValueError("n must be non-zero")
    if s < 0.0 and (n != int(n) or int(n) % 2 == 0):
        raise ValueError("negative s requires an odd integer n")
    if s == 0.0 and n < 0.0:
        raise ValueError("0 has no root with negative n (division by zero)")
    return s, n

def validate_power(x, y):
    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)
    x, y = ensure_not_all(0, x, y)
    if x == 1 and y == INF:
        raise ValueError("x, y cannot be 1, INF")
    elif x == INF and y == 0:
        raise ValueError("x, y cannot be INF, 0")
    elif x == 0 and y < 0:
        raise ValueError("x cannot equal 0 if y<0")
    elif x < 0 and type(y) != int:
        raise ValueError("x cannot be negative if y is not an integer")
    else:
        return x, y

def validate_multiply(x, y):
    """Return x, y if valid (real and not 0 and INF).
    Else raise ValueError"""
    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)
    if (x == 0 and y == INF) or (x == INF and y == 0):
        raise ValueError("x, y cannot be 0, INF in either order")
    else:
        return x, y