from closing import closing
from opening import opening
def texture_segmentation(image, structuring_element):
    closed_img = closing(image, structuring_element)
    return opening(closed_img, structuring_element)