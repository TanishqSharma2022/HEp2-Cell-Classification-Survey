from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def getYCbCr(filepath):
    image = Image.open(filepath).convert('YCbCr')
    y, cb, cr = image.split()
    return np.array(y)


def getPlot(image):
    plt.figure(figsize=(4, 4))
    plt.imshow(image)
    plt.show()


def string_to_label(label):
    match label:
        case "homogeneous":
            return 1
        case "fine_speckled":
            return 2
        case "centromere":
            return 3
        case "nucleolar":
            return 4
        case "coarse_speckled":
            return 5
        case "cytoplasmatic":
            return 6
        case _:
            return "No Match"


    

def string_to_target(target):
    match target:
        case "Centromere":
            return 1
        case "Golgi":
            return 2
        case "Homogeneous":
            return 3
        case "Nucleolar":
            return 4
        case "NuMem":
            return 5
        case "Speckled":
            return 6
        case _:
            return "No Match"