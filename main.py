import matplotlib.pylab as plt
import numpy as np

# reading the image
img = plt.imread("fruits.jpg")
# img.shape ==> (438, 700, 3)
# first two dimension of this array is x and y position while third is RGB



def show_image(imgarray, **kwargs):
    """
        plot the image
    """
    y = imgarray.shape[0]
    x = imgarray.shape[1]
  
    plt.figure(figsize = (x,y))
    plt.imshow(imgarray,  interpolation=None, **kwargs)
    plt.show()


def crop_img(imgarray, top=0, left=0,right=0, bottom=0):
    y = imgarray.shape[0]
    x = imgarray.shape[1]
    newimg = imgarray[top:y-bottom,left:x-right, :]
    return newimg.shape

print(crop_img(img, 100,100,100,100))