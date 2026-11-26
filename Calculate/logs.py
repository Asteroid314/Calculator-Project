from .constants import *

def _check(argument, base):
    # check to ensure argument is positive (not including 0) and finite and is a number, and also checks if the base is not 1 and is also + and finite
    try:
        if not 0.0 < argument < INF:
            raise ValueError
        if not 0.0 < base < INF or base==1:
            raise ValueError
    except ValueError:
        print("Problem with the base and/or argument (base cannot be 1 and must be positive and finite, argument must be a positive and finite)")

# this algorithm takes a rough guess of ln(x) and nudges it to make it more accurate
# if you dont get it, me neither, read https://en.wikipedia.org/wiki/Halley's_method#
# i just used the formulas there
def _halley(x, half):
    t = E ** half
    q = x / t
    return 2.0 * (half + (q - t) / (q + t))

def _ln(x):
    # if x is close to 1, adds up a few small numbers to converge towards the answer
    if 0.99 < x < 1.01:
        u = (x - 1.0) / (x + 1.0) # u is half the difference from x to 1, using midpoint formula
        z = u * u
        # https://en.wikipedia.org/wiki/Logarithm#Calculation
        # this series basically converges to ln(x)
        # according to the taylor series, ln(1+u) = u - u^2/2 + u^3/3 - ... +- u^n/n
        # ln(1-u) = -u - u^2/2 - u^3/3 - ... - u^n/n
        # ln(1+u) - ln(1-u) = ln((1+u)/(1-u)) = ln(x), because u = (x-1)/(x+1)
        # subtracting cancels the even powers and doubles the odd ones:
        # ln(x) = 2(u + u^3/3 + u^5/5 + u^7/7 + ...)
        # z = u^2, and we stop at u^7 because later terms are too small to matter
        return 2.0 * u * (1.0 + z * (1/3 + z * (1/5 + z / 7)))

    # makes a quick guess if not close to 1 (this is half of it), then improve it
    half = (x ** H - 1.0) * HALF_OVER_H
    return _halley(x, half)

def log(argument, base=10):
    if base == 10 and 0.0 < argument < INF:
        return _ln(argument) / LN10
    _check(argument, base)
    return _ln(argument) / _ln(base) #ts change of base
