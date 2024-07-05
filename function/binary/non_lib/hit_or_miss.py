from . import erosion
import numpy as np
def hit_or_miss (image, structuring_element):
    # Tạo các bản sao của kernel
    b1 = structuring_element.copy()
    b2 = structuring_element.copy()
    
    # Thay đổi giá trị -1 thành 0 trong bản sao b1 của kernel
    b1[b1==-1] = 0
    # Thay đổi giá trị -1 thành 1 và 0 thành -1 trong bản sao b2 của kernel
    b2[b2==-1] = 1
    b2[b2==0] = -1

    # Thực hiện phép xói mòn với kernel b1, b2 trên ảnh đầu vào
    a = erosion(image,b1)
    b = erosion(~(np.where(image == 255, 1, image)), b2)
    
    # Lấy phép giao giữa 2 ảnh đã xói mòn
    hitmiss_img = np.logical_and(a,b)
    return np.uint8(hitmiss_img)