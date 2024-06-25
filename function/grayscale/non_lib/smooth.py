from opening import opening
from closing import closing

def smoothing(image, structuring_element):
    result = opening(image, structuring_element)
    result = closing(result, structuring_element)
    return result