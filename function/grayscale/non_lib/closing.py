from dilation import dilation
from erosion import erosion

def closing (image, structuring_element):
    closed_image = dilation(image, structuring_element)
    closed_image = erosion(closed_image, structuring_element)
    return closed_image