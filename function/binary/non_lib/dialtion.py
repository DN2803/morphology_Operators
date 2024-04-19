import numpy as np
def dialation(image, structuring_element):
    # Get dimensions of the image and the structuring element
    image_height, image_width = image.shape
    struct_height, struct_width = structuring_element.shape

    # Initialize an empty array to store the dilated image
    dilated_image = np.zeros_like(image)

    # Loop through each pixel in the image
    for i in range(image_height):
        for j in range(image_width):
            # Check if the structuring element fits entirely within the image at position (i, j)
            if (i - struct_height // 2 >= 0 and i + struct_height // 2 < image_height and
                j - struct_width // 2 >= 0 and j + struct_width // 2 < image_width):
                # Check if the structuring element matches the image at position (i, j)
                if np.all(image[i - struct_height // 2:i + struct_height // 2 + 1,
                              j - struct_width // 2:j + struct_width // 2 + 1] * structuring_element):
                    # If it matches, set the corresponding pixel in the dilated image to 1
                    dilated_image[i, j] = 1

    return dilated_image
