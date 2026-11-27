from .registry import register
from .validation import *
from .constants import *

@register("sqrt")
def sqrt(s):
    """Return principal square root of s (positive number whose square is s). s must be real and >= 0."""
    s = check_real(s, "s", allow_inf=True)
    s = ensure_range(0, INF, True, True, s)
    if s == 0.0: return 0.0 # Prevent possible ZeroDivisionError
    
    # Scale s into [1, 4) tracking matching factor of 2
    scale, t = 1.0, s
    while t >= 4.0:
        t *= 0.25
        scale *= 2.0
    while t < 1.0:
        t *= 4
        scale *= 0.5

    # sqrt(t) is within ~15% of (1 + t) / 2 on [1,4)
    x = 0.5 * (1.0 + t)

    # Newton
    for _ in range(5):
        x = 0.5 * (x + t / x)

    return x * scale

@register("cbrt")
def cbrt(s):
    """Return principal cube root of s (number whose cube is s). s must be real."""
    s = check_real(s, "s", allow_inf=True)

    if s == 0.0:
        return 0.0 # Prevent possible ZeroDivisionError

    negative = s < 0.0
    t = -s if negative else s

    # Scale t into [1, 8)
    scale = 1.0
    while t >= 8.0:
        t *= 0.125
        scale *= 2.0
    while t < 1.0:
        t *= 8.0
        scale *= 0.5

    # Starting guess (worst error about 11%)
    x = 1.0 + (t - 1.0) / 7.0

    # Newton's method
    for _ in range(5):
        x = x - (x - t / (x * x)) / 3.0

    result = x * scale
    return -result if negative else result

def _pow2(k):
    """Exact 2**k for -1074 <= k <= 1023 (integer k)."""
    base = 2.0 if k >= 0 else 0.5
    k = abs(k)
    r = 1.0
    while k:
        if k & 1:
            r *= base
        base *= base
        k >>= 1
    return r

def _scale2(x, k):
    """x * 2**k with correct overflow/underflow and rounding."""
    if k> 2200:
        k = 2200
    elif k < -2300:
        k = -2300
    while k > 1000:
        x *= TWO1000
        k -= 1000
    while k < -1000:
        x *= TWO_M1000
        k += 1000
    return x * _pow2(k)

def _decompose(a):
    """a > 0 finite -> (m, e) with a = m * 2**e, m in [sqrt(1/2), sqrt(2))."""
    e = 0
    while a >= TWO64:
        a *= TWO_M64
        e += 64
    while a < TWO_M64:
        a *= TWO64
        e -= 64
    while a >= 2.0:
        a *= 0.5
        e += 1
    while a < 1.0:
        a *= 2.0
        e -= 1
    if a > SQRT2:
        a *= 0.5
        e += 1
    return a, e

def _ln_m(m):
    """ln(m) for m in [sqrt(1/2), sqrt(2)) via 2*atanh((m-1)/(m+1))."""
    f = (m - 1.0) / (m + 1.0)
    f2 = f * f
    p = 1.0 / 25.0
    for j in range(11, 0, -1):
        p = p * f2 + 1.0 / (2 * j + 1)
    return 2.0 * f + 2.0 * f * f2 * p

def _exp(w):
    """e**w, w finite."""
    k = round(w / 0.6931471805599453)
    r = (w - k * LN2_HI) - k * LN2_LO
    q = 1.0
    for i in range(16, 1, -1):
        q = 1.0 + q * r / i
    return _scale2(1.0 + r * q, k)

def _split(a):
    c = 134217729.0 * a
    hi = c - (c - a)
    return hi, a - hi

def _two_prod(a, b):
    """(p, err) with a*b == p + err exactly."""
    p = a * b
    ah, al = _split(a)
    bh, bl = _split(b)
    err = ((ah * bh - p) + ah * bl + al * bh) + al * bl
    return p, err

def _ipow(x, p):
    r = 1.0
    while p:
        if p & 1:
            r *= x
        x *= x
        p >>= 1
    return r

def _nth_root(s, n, polish=True):
    """Core routine. Requires validated input.
       I don't want to explain how this works."""
    if n < 0.0:
        return 1.0 / nth_root(s, -n, polish)
    if n == 1.0:
        return s
    if s == 0.0:
        return 0.0
    negative = s < 0.0

    a = -s if negative else s

    m, e = _decompose(a)
    lnm = _ln_m(m)

    # Saturate absurd results before doing exact arithmetic
    W = (e * 0.6931471805599453 + lnm) / n
    if W > 2000.0:
        return -float("inf") if negative else float("inf")
    if W < -2000.0:
        return -0.0 if negative else 0.0

    is_int = n == int(n) and n < 4503599627370496.0
    if is_int:
        N = int(n)
        k = round(e / n)
        d = e - k * N
        u = (d * LN2_HI + (d * LN2_LO + lnm)) / n
        x = _exp(u)
        if polish and N <= 1000:
            t = m * _pow2(d)
            for _ in range(2):
                x = x - (x - t / _ipow(x, N - 1)) / n
    else:
        k = round(e / n)
        if k != 0:
            p, err = _two_prod(float(k), n)
            d = (e - p) - err
        else:
            d = float(e)
        x = _exp((d * LN2_HI + (d * LN2_LO + lnm)) / n)

    r = _scale2(x, k)
    return -r if negative else r

@register("nth_root")
def nth_root(s, n, polish=True):
    """Return principal n-th root of s (number whose n-th power is s). s and n must satisfy various criteria (see validate_nth_root)."""
    s, n = validate_nth_root(s, n)
    return _nth_root(s, n, polish)