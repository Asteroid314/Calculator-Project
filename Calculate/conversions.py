from .constants import *
from .validation import *
from .registry import register
from .roots import _two_prod

def _prepare(x):
    """Validate x and return it as a float."""
    x = check_real(x)
    if isinstance(x, int):
        try:
            return float(x)
        except OverflowError:
            raise ValueError("x is too large to convert to a float") from None
    return x

def _multiply(x, hi, lo):
    """Return x * (hi + lo) with rounding (error under 1 ulp)."""
    if x == 0.0:
        return x # Preserves sign of -0.0
    ax = abs(x)
    if ax >= BIG:
        x *= DOWN
        back = UP
    elif ax < SMALL:
        x *= UP
        back = DOWN
    else:
        back = 1.0
    p, err = _two_prod(x, hi)
    result = (p + (err + x * lo)) * back
    if result == INF or result == -INF:
        raise OverflowError("result is too large to represent as a float")
    return result

@register("deg_to_rad")
def degrees_to_radians(x):
    """Convert degrees to radians."""
    return _multiply(_prepare(x), RAD_HI, RAD_LO)

@register("rad_to_deg")
def radians_to_degrees(x):
    """Convert radians to degrees. Overflow error if the result exceeds
    the float range."""
    return _multiply(_prepare(x), DEG_HI, DEG_LO)
