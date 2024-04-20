from PIL import Image
import numpy as np
import os
import os.path as p
from pathlib import Path
from . import dilation
from . import erosion

def gray2binary(gray):
    return (127 < gray) & (gray <= 255)
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    if (typeofOperator == "Dilation"):
        return dilation.dilation(image, structuring_element = structuring_element)
    elif (typeofOperator == "Erosion"): 
        return erosion.erosion(image, structuring_element=structuring_element)
    return result