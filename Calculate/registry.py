OPERATIONS = {}

def register(name):
    def decorator(func):
        OPERATIONS[name] = func
        return func
    return decorator

def execute(name, *operands):
    try:
        operation = OPERATIONS[name]

    except KeyError:
        raise ValueError(
            f"Unknown operation '{operation}'"
        )

    return operation(*operands)