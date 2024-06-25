from dilation import dilation
from erosion import erosion

def opening (image, structuring_element):
    opend_image = erosion(image, structuring_element)
    opend_image = dilation(opend_image, structuring_element)
    return opend_image