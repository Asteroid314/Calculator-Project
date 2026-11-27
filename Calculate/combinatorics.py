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

@register("choose")
def choose(n, r):
    """Return n!/(r!*(n-r)!), provided n, r are integers,
    0 <= n and 0 <= r <= n."""
    n = ensure_integer(n, "n", allow_inf=False)
    r = ensure_integer(r, "r", allow_inf=False)
    n = ensure_range(0, INF, True, False, n)
    r = ensure_range(0, n, True, True, r)

    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result = (result * (n - i + 1)) // i
    return result