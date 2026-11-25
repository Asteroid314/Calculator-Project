from validation import *
from registry import register
from constants import *

def _cordic(*operands):
    z = get_unary_operand(operands)
    # Wrap any input angle into one full period [0, 2pi]
    z %= 2 * PI

    # Wrap angle into [-pi, +pi]
    if z > PI:
        z -= 2 * PI
    elif z < -PI:
        z += 2 * PI

    # Pre-rotate into [-pi/2, +pi/2] and initialise.
    if z > PI / 2:
        x, y = 0, CORDIC_K
        z -= PI / 2
    elif z < -PI / 2:
        x, y = 0, -CORDIC_K
        z += PI / 2
    else:
        x, y = CORDIC_K, 0

    # Main loop - converge on exact angle
    for i in range(CORDIC_ITERATIONS):
        step = CORDIC_ARCTANS[i] if i < len(CORDIC_ARCTANS) else (2 ** -i)
        if z >= 0:
            xNext, yNext, zNext = x - (y * (2 ** -i)), y + (x * (2 ** -i)), z - step
        else:
            xNext, yNext, zNext = x + (y * (2 ** -i)), y - (x * (2 ** -i)), z + step
        x, y, z = xNext, yNext, zNext
    return round(x, 14) + 0.0, round(y, 14) + 0.0

@register("sine")
def sine(*operands):
    x = get_unary_operand(operands)
    ensure_numeric(x)
    return _cordic(x)[1]

@register("cosine")
def cosine(*operands):
    x = get_unary_operand(operands)
    ensure_numeric(x)
    return _cordic(x)[0]

@register("tangent")
def tangent(*operands):
    x = get_unary_operand(operands)
    ensure_numeric(x)
    cordic_result = _cordic(x)
    ensure_not_zero(cordic_result[0])
    return cordic_result[1] / cordic_result[0]

@register("arcsine")
def arcsine(*operands):
    x = get_unary_operand(operands)
    ensure_numeric(x)
    negative = x < 0.0
    ax = abs(x)
    if ax <= 0.5:
        if ax < 1e-8:
            return x
        z = ax * ax
        p = z * (
            pS0 + z * (pS1 + z * (pS2 + z * (pS3 + z * (pS4 + z * pS5))))
        )
        q = 1.0 + z * (qS1 + z * (qS2 + z * (qS3 + z * qS4)))
        result = ax + ax * (p / q)
    else:
        z = 0.5 * (1.0 - ax)
        s = z ** 0.5
        p = z * (
            pS0 + z * (pS1 + z * (pS2 + z * (pS3 + z * (pS4 + z * pS5))))
        )
        q = 1.0 + z * (qS1 + z * (qS2 + z * (qS3 + z * qS4)))
        r = p / q
        result = (PI / 2) - 2.0 * (s + s * r)
    return -result if negative else result