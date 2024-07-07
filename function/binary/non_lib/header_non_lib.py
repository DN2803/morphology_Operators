from . import dilation
from . import erosion
from . import opening
from . import closing
from . import hit_or_miss
from . import boundary_extraction
from . import region_filling
from . import connect_components
from . import convex_hull
from . import thinning
from . import thickening
from . import skeletons
from . import pruning
from . import reconstruction
import numpy as np
def gray2binary(gray):
    return (127 < gray) & (gray <= 255)
def binary_morphology(image, structuring_element, typeofOperator = "Dilation"):
    result = np.zeros_like(image)
    if (typeofOperator == "Dilation"):
        return dilation.dilation(image, structuring_element = structuring_element)
    elif (typeofOperator == "Erosion"): 
        return erosion.erosion(image, structuring_element= structuring_element)
    elif (typeofOperator == "Opening"):
        return opening.opening(image, structuring_element = structuring_element)
    elif (typeofOperator == "Closing"):
        return closing.closing(image, structuring_element = structuring_element)
    elif (typeofOperator == "Hit or Miss"): 
        return hit_or_miss.hit_or_miss(image, structuring_element)
    elif (typeofOperator == "Boundary Extraction"):
        return boundary_extraction.boundary_extraction(image, structuring_element)
        
    elif (typeofOperator == "Region Filling"): 
        return region_filling.region_fill(image, structuring_element )
    elif (typeofOperator == "Extraction of Connected Components"): 
        return connect_components.connect_components(image, structuring_element)
    
    elif (typeofOperator == "Convex Hull"):
        return convex_hull.convex_hull(image)
    elif (typeofOperator == "Thinning"): 

        return thinning.thinning(gray2binary(image))
    elif (typeofOperator == "Thickening"): 
        return result
    elif (typeofOperator == "Skeletons"): 
        return skeletons.skeletons(image,structuring_element)
    elif (typeofOperator == "Reconstruction"): 
        return reconstruction.reconstruction(image, structuring_element)
    elif (typeofOperator == "Pruning"): 
        return result
    
    return result