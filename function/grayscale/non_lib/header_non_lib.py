from dilation import dilation
from erosion import erosion
from opening import opening
from closing import closing
from smooth import smoothing
from gradient import gradient
from tophat import tophat
from segmentation import texture_segmentation
from granulometry import granulometry
from reconstruction import reconstruction

def grayscale_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    if (typeofOperator == "Dilation"):
        return dilation(image, structuring_element)
    elif (typeofOperator == "Erosion"): 
        return erosion(image, structuring_element)
    elif (typeofOperator == "Opening"):
        return opening(image, structuring_element)
    elif (typeofOperator == "Closing"):
        return closing(image, structuring_element)
    elif (typeofOperator == "Smoothing"):    
        return smoothing (image, structuring_element)
    elif (typeofOperator == "Gradient"): 
        return gradient(image, structuring_element)
    elif (typeofOperator == "Top Hat"): 
        return tophat(image, structuring_element)
    elif (typeofOperator ==  "Textual segmentation"): 
        return texture_segmentation(image, structuring_element)
    elif (typeofOperator == "Granulometry"): 
        return granulometry(image, structuring_element)
    elif (typeofOperator == "Recontruction"): 
        return reconstruction(image, structuring_element)
    return result