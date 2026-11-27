from .validation import *
from .registry import register
from .constants import *
from .roots import sqrt

def _clean(value, eps=1e-14):
    """Reduces values below eps in magnitude to 0."""
    return 0.0 if abs(value) < eps else value

def _reduce_angle(z):
    """Return (n, r) with z = n*(pi/2) + r and r in [-pi/4, pi/4].
       Reduction is accurate to |z| within 1.6 million."""
    n = round(z * INV_PIO2)
    r = z - n * PIO2_1
    r -= n * PIO2_2
    r -= n * PIO2_3
    r -= n * PIO2_3T
    return n, r

def _cordic_cos_sin(z):
    """Return (cos z, sin z) for an angle z in radians, using CORDIC.
    
       Reduces z to [-pi/4, pi/4] with extended precision pi/2. 
       Starts from a vector rotated by n quarter-turns 
       Performs CORDIC_ITERATIONS rotations. CORDIC_K must be the 
       product of 1/sqrt(1 + 2^-2i) over those iterations (pre-computed)."""

    n, z = _reduce_angle(z)
    x, y = CORDIC_START[n % 4]

    # Main loop - converge on exact angle
    for i in range(CORDIC_ITERATIONS):
        t = 2.0 ** -i
        d = 1 if z >= 0 else -1
        x, y, z = x - d * y * t, y + d * x * t, z - d * CORDIC_ARCTANS[i]
    return _clean(x), _clean(y)

@register("sine")
def sine(x):
    """Return sine of angle x (radians). x must be real."""
    x = check_real(x, "x")
    return _cordic_cos_sin(x)[1]

@register("cosine")
def cosine(x):
    """Return cosine of angle x (radians). x must be real."""
    x = check_real(x, "x")
    return _cordic_cos_sin(x)[0]

@register("tangent")
def tangent(x):
    """Return tangent of angle x (radians). x must be real and not an odd multiple of pi/2."""
    x = check_real(x, "x")
    cordic_result = _cordic_cos_sin(x)
    cordic_result[0] = ensure_not_all(0, [cordic_result[0]])
    return cordic_result[1] / cordic_result[0]

@register("arcsine")
def arcsine(x):
    """Return arcsine (radians) of x. x must be real and -1 <= x <= 1."""
    x = check_real(x, "x")
    x = ensure_domain(x, 1)
    negative = x < 0.0
    ax = abs(x)
    if ax <= 0.5:
        if ax < 2.0 ** -26:
            return x
        z = ax * ax
    else:
        z = 0.5 * (1.0 - ax)
    p = z * (ASIN_P0 + z * (ASIN_P1 + z * (ASIN_P2 + z * (ASIN_P3 + z * (ASIN_P4 + z * ASIN_P5)))))
    q = 1.0 + z * (ASIN_Q1 + z * (ASIN_Q2 + z * (ASIN_Q3 + z * ASIN_Q4)))    
    r = p / q
    if ax <= 0.5:
        result = ax + ax * r
    else:
        s = sqrt(z)
        result = PI / 2 - 2.0 * (s + s * r)
    return -result if negative else result