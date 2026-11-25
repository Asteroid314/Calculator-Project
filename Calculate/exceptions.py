class VariableTypeError(TypeError):

    def __init__(self, value, index = 0):
        self.value = value
        self.index = index

        super().__init__(
            f"Argument {index} has invalid type: {value}"
        )

class VariableValueError(ValueError):

    def __init__(self, value, index = 0):
        self.value = value
        self.index = index

        super().__init__(
            f"Argument {index} has invalid value: {value}"
        )
        