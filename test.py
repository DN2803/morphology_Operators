import numpy as np
import matplotlib.pyplot as plt

def dilate(image, struct_elem):
    padded_image = np.pad(image, 1, mode='constant')
    dilated_image = np.zeros_like(image)
    
    for i in range(1, padded_image.shape[0] - 1):
        for j in range(1, padded_image.shape[1] - 1):
            if padded_image[i, j] == 1:
                for si in range(struct_elem.shape[0]):
                    for sj in range(struct_elem.shape[1]):
                        if struct_elem[si, sj] == 1:
                            dilated_image[i - 1 + si, j - 1 + sj] = 1
    
    return dilated_image

def erode(image, struct_elem):
    padded_image = np.pad(image, 1, mode='constant')
    eroded_image = np.zeros_like(image)
    
    for i in range(1, padded_image.shape[0] - 1):
        for j in range(1, padded_image.shape[1] - 1):
            match = True
            for si in range(struct_elem.shape[0]):
                for sj in range(struct_elem.shape[1]):
                    if struct_elem[si, sj] == 1 and padded_image[i - 1 + si, j - 1 + sj] != 1:
                        match = False
                        break
                if not match:
                    break
            if match:
                eroded_image[i - 1, j - 1] = 1
    
    return eroded_image

def connected_components(binary_image):
    struct_elem = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]], dtype=int)
    
    label = 1
    labels = np.zeros_like(binary_image)
    
    # Copy the binary image
    working_image = binary_image.copy()
    
    while np.any(working_image):
        # Find a seed pixel
        seed = np.zeros_like(working_image)
        seed[working_image == 1] = 1
        seed = seed.astype(np.uint8)
        
        component = np.zeros_like(working_image)
        while True:
            new_component = dilate(component, struct_elem)
            new_component = new_component & binary_image
            if np.array_equal(new_component, component):
                break
            component = new_component
        
        # Label the component
        labels[component == 1] = label
        working_image[component == 1] = 0
        label += 1
    
    return label - 1, labels

# Example usage
binary_image = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
], dtype=int)

num_labels, labeled_image = connected_components(binary_image)

# Visualize the result
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Binary Image')
plt.imshow(binary_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Connected Components')
plt.imshow(labeled_image, cmap='nipy_spectral')

plt.show()

print("Number of labels:", num_labels)
print("Labeled Image:\n", labeled_image)
