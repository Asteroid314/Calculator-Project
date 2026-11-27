from .validation import *
from .registry import register

@register("factorial")
def factorial(x):

    x = check_real(x, "x", allow_inf=True)
    x = ensure_integer(x, "x", allow_inf=True)
    x = ensure_range(0, INF, True, True, x)

    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
