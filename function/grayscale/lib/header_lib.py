import cv2
def grayscale_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    if (typeofOperator == "Dilation"):
        return cv2.dilate(image, structuring_element)
    elif (typeofOperator == "Erosion"): 
        return cv2.erode(image, structuring_element)
    return result
