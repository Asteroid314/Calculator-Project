from .registry import register
from .validation import *

@register("sqrt")
def sqrt(*operands):
    s = get_unary_operand(operands)
    ensure_numeric(s)
    ensure_non_negative(s)
    if s == 0.0: return 0.0 # Prevent possible ZeroDivisionError
    
    # Scale s into [1, 4) tracking matching factor of 2
    scale, t = 1.0, s
    while t >= 4.0: t, scale *= 0.25, 2.0
    while t < 1.0: t, scale *= 4, 0.5

    # sqrt(t) is within ~15% of (1 + t) / 2 on [1,4)
    x = 0.5 * (1.0 + t)

    # Newton
    for _ in range(5):
        x = 0.5 * (x + t / x)

    return x * scale