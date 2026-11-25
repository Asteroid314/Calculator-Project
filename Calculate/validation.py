from exceptions import VariableValueError, VariableTypeError

def ensure_numeric(value, index = 0):
    """Ensure value is of type int or float."""
    if not isinstance(value, (int, float)):
        raise VariableTypeError(value, index)

def ensure_integer(value, index = 0):
    """Ensure value is of type int."""
    if not isinstance(value, int):
        raise VariableTypeError(value, index)

def ensure_non_negative(value, index = 0):
    """Ensure value is greater than or equal to zero."""
    if value < 0:
        raise VariableValueError(value, index)

def ensure_probability(value, index = 0):
    """Ensure value is in [-1, 1]."""
    if value < -1 or value > 1:
        raise VariableValueError(value, index)

def ensure_not_zero(value, index = 0):
    """Ensure value is not zero."""
    if value == 0:
        raise ZeroDivisionError

def ensure_not_both_zero(value0, value1):
    """Ensure two values are not both zero."""
    if value0 == 0 and value1 == 0:
        raise ValueError(
            "Both values cannot be zero."
        )

def ensure_positive(value, index = 0):
    """Ensure value is greater than zero."""
    if value <= 0:
        raise VariableValueError(value, index)

def ensure_operand_count(operands, expected):
    """Ensure the expected number of operands have been received."""
    if len(operands) != expected:
        raise ValueError(
            f"Expected {expected} operands, got {len(operands)}."
        )

def ensure_domain(value, max):
    """Ensure value is less than or equal to max in magnitude."""
    if abs(value) > max:
        raise ValueError(
            f"Domain error: |x| must be <= {max} (currently {value})."
        )

def get_unary_operand(operands):
    ensure_operand_count(operands, 1)
    return operands

def get_binary_operands(operands):
    ensure_operand_count(operands, 2)
    return operands