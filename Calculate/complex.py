from .registry import register
from .validation import *

class Complex:
    def __init__(self, re, im):
        self.Re = re
        self.Im = im

@register("complex_add")
def complex_add(x, y):
    # Need to check x and y are of type Complex.
    result = Complex(x.Re + y.Re, x.Im + y.Im)
    return result