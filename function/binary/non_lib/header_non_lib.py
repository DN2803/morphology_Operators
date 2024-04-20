from . import dilation
from . import erosion
from . import opening
from . import closing

def gray2binary(gray):
    return (127 < gray) & (gray <= 255)
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    if (typeofOperator == "Dilation"):
        return dilation.dilation(image, structuring_element = structuring_element)
    elif (typeofOperator == "Erosion"): 
        return erosion.erosion(image, structuring_element= structuring_element)
    elif (typeofOperator == "Opening"):
        return opening.opening(image, structuring_element = structuring_element)
    elif (typeofOperator == "Closing"):
        return closing.closing(image, structuring_element = structuring_element)
    return result