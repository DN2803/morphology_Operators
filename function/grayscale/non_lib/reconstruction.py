from dilation import dilation
from erosion import erosion
import numpy as np 
def reconstruction (image, structuring_element):
    # Khởi tạo kết quả ban đầu là hình ảnh đầu vào
    result = image.copy()
    
    # Thực hiện dilation ban đầu
    dilated = dilation(result, structuring_element)
    
    # Lặp lại quá trình thực hiện dilation và erosion cho đến khi không còn thay đổi nào nữa
    while not np.array_equal(result, dilated):
        result = dilated.copy()
        dilated = dilation(result, structuring_element)
        dilated = erosion(dilated, structuring_element)    
    return result