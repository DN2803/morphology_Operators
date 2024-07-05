from . import dilation
from . import erosion
import numpy as np 
def reconstruction_dilation (image, structuring_element):
    # Khởi tạo kết quả ban đầu là hình ảnh đầu vào
    result = image.copy()
    
    # Thực hiện dilation ban đầu
    recon = dilation.dilation(result, structuring_element)
    prev = np.copy(recon)
        
    # Lặp lại quá trình tái tạo cho đến khi không còn thay đổi
    while not np.array_equal(prev, recon):
        prev = np.copy(recon)
        # Áp dụng toán dilation giữa G và B
        recon = dilation.dilation(recon, structuring_element)
        # Áp dụng toán erosion giữa kết quả và ảnh đầu vào f
        recon = erosion.erosion(recon, image)
        return recon