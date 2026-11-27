from .validation import *
from .registry import register

@register("add")
def add(x, y):
    """Return sum of x and y. x, y must be real."""
    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)

    return x + y

@register("subtract")
def subtract(x, y):
    """Return difference between x and y. x, y must be real but not both infinite."""
    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)
    x, y = ensure_not_all(INF, [x, y])

    return x - y

@register("multiply")
def multiply(x, y):
    """Return product of x and y. x, y must satisfy various criteria (see validate_multiply)."""
    x, y = validate_multiply(x, y)

    return x * y

@register("divide")
def divide(x, y):
    """Return quotient of x and y. x, y must be real. y must be non-zero. x, y cannot both be infinite."""
    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)
    y = ensure_not_all(0, [y])
    x, y = ensure_not_all(INF, [x, y])

    return x / y

@register("power")
def power(x, y):
    """Return y-th power of x. x, y must satisfy various criteria (see validate_power)."""
    x, y = validate_power(x, y)

    return x ** y
    