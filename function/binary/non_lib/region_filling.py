import numpy as np
from scipy.ndimage import find_objects
from scipy.ndimage import label
from . import dilation
def find_seed_bounding_box_center(image):
    """
    Find the seed point as the center of the bounding box of the foreground region.
    
    Parameters:
    image: np.ndarray
        The binary input image.
        
    Returns:
    seed_point: tuple
        The (row, column) coordinates of the seed point.
    """
    labeled_image, num_features = label(image)
    slices = find_objects(labeled_image)
    
    # Assuming the first labeled object is the target region
    bbox = slices[0]
    
    bbox_center = ((bbox[0].start + bbox[0].stop) // 2, (bbox[1].start + bbox[1].stop) // 2)
    
    return bbox_center

def region_fill(image, structuring_element):
    seed_point = find_seed_bounding_box_center(image)
    print (seed_point)
    # Create a marker image with the seed point
    marker = image
    #marker[seed_point] = 1
    

    
    marker = dilation.dilation(marker, structuring_element)
    marker = marker & np.logical_not(image)
    
    # Iteratively dilate the marker image and intersect with the original image
    prev_marker = np.zeros_like(marker)
    while not np.array_equal(marker, prev_marker):
        prev_marker = marker.copy()
        marker = dilation.dilation(marker, structuring_element)
        marker = marker & np.logical_not(image)
    return marker 

        