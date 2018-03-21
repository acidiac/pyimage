import matplotlib.pylab as plt
import numpy as np

# reading the image
img = plt.imread("fruits.jpg")
# img.shape ==> (438, 700, 3)
# first two dimension of this array is x and y position while third is RGB



def showImage(imgarray, **kwargs):
    """
        plot the image
    """
    y = imgarray.shape[0]
    x = imgarray.shape[1]
  
    plt.figure(figsize = (x,y))
    plt.imshow(imgarray,  interpolation=None, **kwargs)
    plt.show()
showImage(img)