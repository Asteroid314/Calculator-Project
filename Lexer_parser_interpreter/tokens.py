class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def getValue(self):
        return self.value

class Variable:
    def __init__(self, name):
        self.name = name
        self.type = 'VAR'
        self.value = 0

    def getValue(self):
        return self.value

    def setValue(self, toSet):
        if type(toSet) == int or type(toSet) == float:
            self.value = toSet
            return toSet
        else:
            raise TypeError("The type of data you tried to enter was incorrect, please try again.")
