from opening import opening
from closing import closing

def granulometry (image, structuring_element):
    closed = closing(image, structuring_element)
    opened = opening(image, structuring_element)
    return closed - opened