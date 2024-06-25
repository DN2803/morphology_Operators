from dilation import dilation
from erosion import erosion

def gradient (image, structuring_element):
    dialated_img = dilation(image, structuring_element)
    eroded_img = erosion(image, structuring_element)
    return dialated_img - eroded_img
