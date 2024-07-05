from . import dilation
from . import erosion
from . import opening
from . import closing
from . import smooth
from . import gradient
from . import tophat
from . import segmentation
from . import granulometry
from . import reconstruction

def grayscale_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    if (typeofOperator == "Dilation"):
        return dilation.dilation(image, structuring_element)
    elif (typeofOperator == "Erosion"): 
        return erosion.erosion(image, structuring_element)
    elif (typeofOperator == "Opening"):
        return opening.opening(image, structuring_element)
    elif (typeofOperator == "Closing"):
        return closing.closing(image, structuring_element)
    elif (typeofOperator == "Smoothing"):    
        return smooth.smoothing (image, structuring_element)
    elif (typeofOperator == "Gradient"): 
        return gradient.gradient(image, structuring_element)
    elif (typeofOperator == "Top Hat"): 
        return tophat.tophat(image, structuring_element)
    elif (typeofOperator ==  "Textual segmentation"): 
        return segmentation.texture_segmentation(image, structuring_element)
    elif (typeofOperator == "Granulometry"): 
        return granulometry.granulometry(image, structuring_element)
    elif (typeofOperator == "Reconstruction"): 
        return reconstruction.reconstruction_dilation(image, structuring_element)
    return result