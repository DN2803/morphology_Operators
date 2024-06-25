from opening import opening
def tophat(image, structuring_element):
    opened_img = opening(image, structuring_element)
    return image - opened_img