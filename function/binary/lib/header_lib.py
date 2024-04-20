import cv2.ximgproc
import cv2, numpy as np
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = []
    kernel = np.matrix(structuring_element, np.uint8) 
    if (typeofOperator == "Dilation"):
        return cv2.dilate(image, kernel, iterations = 1)
    elif (typeofOperator == "Erosion"): 
        return cv2.erode(image, structuring_element, iterations = 1)
    elif (typeofOperator == "Opening"):
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, structuring_element)
    elif (typeofOperator == "Closing"):
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, structuring_element)
    elif (typeofOperator == "Hit or Miss"): 
        return cv2.morphologyEx(image, cv2.MORPH_HITMISS, structuring_element)
    elif (typeofOperator == "Boundary Extraction"):
        erode = cv2.erode(image, structuring_element, iterations = 1)  #co đối tượng lại
        return image - erode   #áp dụng công thức
    elif (typeofOperator == "Region Filling"): 
        return result
    elif (typeofOperator == "Extraction of Connected Components"): 
        return result
    
    elif (typeofOperator == "Convex Hull"):
        blur = cv2.blur(image, (3, 3)) #blur the image

        _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY) #apply binary thresholding for blur

        # tìm contour trong ảnh threshhold
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Tìm Convex Hull của các contour
        hull = []
        for i in range(len(contours)):
            hull.append(cv2.convexHull(contours[i], False))
        
        # Vẽ Convex Hull lên hình ảnh gốc
        # create an empty black image
        drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
        
        # draw contours and hull points
        for i in range(len(contours)):
            color_contours = (0, 255, 0) # green - color for contours
            color = (255, 0, 0) # blue - color for convex hull
            # draw ith contour
            cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
            # draw ith convex hull object
            cv2.drawContours(drawing, hull, i, color, 1, 8)
        return drawing
    elif (typeofOperator == "Thinning"): 
        return cv2.ximgproc.thinning(image, None, cv2.ximgproc.THINNING_ZHANGSUEN)
    elif (typeofOperator == "Thickening"): 
        return result
    elif (typeofOperator == "Skeletons"): 
        return result
    elif (typeofOperator == "Reconstruction"): 
        return result
    elif (typeofOperator == "Pruning"): 
        return result
    
    return result