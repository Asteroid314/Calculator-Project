from .registry import register
from .validation import *

@register("floor")
def floor(x):
    """Largest integer <= x."""
    x = check_real(x)
    if isinstance(x, int):
        return x
    t = int(x)                     # Truncates towards zero
    return t - 1 if x < t else t   # x < t only for negative non-integer x

@register("ceil")
def ceil(x):
    """Smallest integer >= x."""
    x = check_real(x)
    if isinstance(x, int):
        return x
    t = int(x)
    return t + 1 if x > t else t   # x > t only for positive non-integer x

@register("absolute")
def absolute(x):
    """|x|. Infinity is allowed (|+-inf| = inf); NaN is rejected."""
    x = check_real(x, allow_inf=True)
    if isinstance(x, int):
        return -x if x < 0 else x
    return x if x > 0.0 else 0.0 - x  # 0.0 - (-0.0) == +0.0, so -0.0 becomes +0.0
