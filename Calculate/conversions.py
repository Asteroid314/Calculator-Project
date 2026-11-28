from .constants import *
from .validation import *
from .registry import register

@register("degtorad")
def deg_to_rad(deg):
    return deg * (PI / 180)

@register("radtodeg")
def rad_to_deg(rad):
    return rad / (PI / 180)