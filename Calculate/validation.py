from .exceptions import VariableValueError, VariableTypeError
from .constants import *

def ensure_numeric(value, index = 0):
    """Ensure value is of type int or float."""
    if not isinstance(value, (int, float)):
        raise VariableTypeError(value, index)

def ensure_integer(value, index = 0):
    """Ensure value is of type int."""
    if not isinstance(value, int):
        raise VariableTypeError(value, index)

def ensure_non_negative(value, index = 0):
    """Ensure value is greater than or equal to zero."""
    if value < 0:
        raise VariableValueError(value, index)

def ensure_probability(value, index = 0):
    """Ensure value is in [-1, 1]."""
    if value < -1 or value > 1:
        raise VariableValueError(value, index)

def ensure_not_zero(value, index = 0):
    """Ensure value is not zero."""
    if value == 0:
        raise ZeroDivisionError

def ensure_not_both_zero(value0, value1):
    """Ensure two values are not both zero."""
    if value0 == 0 and value1 == 0:
        raise ValueError(
            "Both values cannot be zero."
        )

def ensure_positive(value, index = 0):
    """Ensure value is greater than zero."""
    if value <= 0:
        raise VariableValueError(value, index)

def ensure_operand_count(operands, expected):
    """Ensure the expected number of operands have been received."""
    if len(operands) != expected:
        raise ValueError(
            f"Expected {expected} operands, got {len(operands)}."
        )

def ensure_domain(value, max):
    """Ensure value is less than or equal to max in magnitude."""
    if abs(value) > max:
        raise ValueError(
            f"Domain error: |x| must be <= {max} (currently {value})."
        )

def ensure_odd_if_neg(index, radicand):
    if radicand < 0:
        if index % 2 == 0:
            raise ValueError(
                f"Even root of negative integer is undefined."
            )

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

def get_unary_operand(operands):
    ensure_operand_count(operands, 1)
    return operands

def get_binary_operands(operands):
    ensure_operand_count(operands, 2)
    return operands