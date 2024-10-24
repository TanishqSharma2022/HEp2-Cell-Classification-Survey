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