from .validation import *
from .registry import register

@register("add")
def add(*operands):
    x, y = get_binary_operands(operands)
    
    ensure_numeric(x, 0)
    ensure_numeric(y, 1)

    return x + y

@register("multiadd")
def multiadd(*operands):
    total = 0
    for idx in range(len(operands)):
        ensure_numeric(operands[idx], idx)
        total += operands[idx]
    return total


@register("subtract")
def subtract(*operands):
    x, y = get_binary_operands(operands)

    ensure_numeric(x, 0)
    ensure_numeric(y, 1)

    return x - y

@register("multiply")
def multiply(*operands):
    x, y = get_binary_operands(operands)

    ensure_numeric(x, 0)
    ensure_numeric(y, 1)

    return x * y

@register("multimultiply")
def multimultiply(*operands):
    product = 1
    for idx in range(len(operands)):
        ensure_numeric(operands[idx], idx)
        product *= operands[idx]
    return product

@register("divide")
def divide(*operands):
    x, y = get_binary_operands(operands)

    ensure_numeric(x, 0)
    ensure_numeric(y, 1)
    ensure_not_zero(y, 1)

    return x / y

@register("power")
def power(*operands):
    x, y = get_binary_operands(operands)

    ensure_numeric(x, 0)
    ensure_numeric(y, 1)
    ensure_not_both_zero(x, y)

    return x ** y
    