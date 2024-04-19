from PIL import Image
import numpy as np
import os
import os.path as p
from pathlib import Path

def gray2binary(gray):
    return (127 < gray) & (gray <= 255)

def Read_Img():
    #lấy địa chỉ thư mục để đọc vào ảnh
    curPath = p.dirname(Path(__file__).parent.absolute().parent)

    while True:
        path = input("Enter your file picture name (file from Data/binary_image): ") #nhap vao ten file ảnh  
        file_dir = Path(curPath + '\\Data\\' + '\\binary_image\\' + path)

        # kiểm tra xem tập tin có tồn tại hay không
        if os.path.isfile(str(file_dir)):
            break 
        else:
            print("Tập tin không tồn tại trong thư mục hiện tại")

    #orig_img=plt.imread(str(file_dir))
    
    img = Image.open(str(file_dir)).convert('L')    # Chuyển sang mức xám
    # Chuyển đổi ảnh sang dạng numpy array
    img_array = np.array(img)

    # Tạo ảnh nhị phân với ngưỡng 127
    binary_img = np.zeros_like(img_array) # Tạo ảnh đen
    binary_img[img_array > 127] = 255 # Đặt các pixel lớn hơn 127 thành trắng
    #binary_img = gray2binary(img_array)

    # Chuyển đổi ảnh nhị phân sang định dạng PIL Image
    binary_img_pil = Image.fromarray(binary_img)

    return binary_img_pil, path
