import cv2, numpy as np
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    kernel = np.matrix(structuring_element, np.uint8) 
    if (typeofOperator == "Dilation"):
        
        return cv2.dilate(image, kernel, iterations = 1)
    elif (typeofOperator == "Erosion"): 
        return cv2.erode(image, structuring_element, iterations = 1)
    return result