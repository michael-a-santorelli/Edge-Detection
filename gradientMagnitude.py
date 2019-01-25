'''
This file contains an gradient magnitude digital image processing function.
This function uses two edge maps, such as horizontal and vertical,
and then computes the gradient magnitude.
This function then returns the gradient magnitude as a 2D numpy array.
An example of the function call for the gradient magnitude is
gradientMagnitude(edgesX, edgesY)
'''
import numpy
from math import sqrt


# Gradient Magnitude function
def gradientMagnitude(img1, img2):

    # Obtain size of image and create shell of output
    imgSize = img1.shape
    gradientMagnitude = numpy.zeros([imgSize[0], imgSize[1]], dtype=numpy.double)

    # Calculate gradient magnitude
    for i in range(imgSize[0]):
        for j in range(imgSize[1]):
            gradientMagnitude[i, j] = sqrt(img1[i, j]**2 + img2[i, j]**2)

    return gradientMagnitude
