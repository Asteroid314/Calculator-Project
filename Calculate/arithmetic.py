from .validation import *
from .registry import register

@register("add")
def add(x, y):
    
    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)

    return x + y

@register("subtract")
def subtract(x, y):

    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)
    x, y = ensure_not_all(INF, x, y)

    return x - y

@register("multiply")
def multiply(x, y):

    x, y = validate_multiply(x, y)

    return x * y

@register("divide")
def divide(x, y):

    x = check_real(x, "x", allow_inf=True)
    y = check_real(y, "y", allow_inf=True)
    y = ensure_not_all(0, y)[0]
    x, y = ensure_not_all(INF, x, y)

    return x / y

@register("power")
def power(x, y):

    x, y = validate_power(x, y)

    return x ** y
    