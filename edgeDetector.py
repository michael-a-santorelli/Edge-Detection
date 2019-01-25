'''
This file contains an edge detection digital image processing function.
This function converts any given image into a grayscaled version and then computes
an edge detection algorithm on it. This function performs an "aesthetically good"
edge detection as opposed to a numerically good edge detection.
The function call for the edge detection is edgeDetector("file_name")
'''
from gradientMagnitude import gradientMagnitude
import cv2
import numpy


# Edge Detection function
def edgeDetector(image: str):

    # Load image as grayscale to operate on intensity values
    img = cv2.imread(image, 0)
    # Blur image to mitigate noise
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    # Obtain horizontal and vertical edges separately using Sobel operators
    edgesX = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
    edgesY = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
    # Calculate edge map using gradient magnitude of horizontal and vertical edges
    edgeMap = gradientMagnitude(edgesX, edgesY)

    img_size = edgeMap.shape

    # Rescale values into 8-bit range
    if(numpy.amax(edgeMap) > 255):
        ratio = numpy.amax(edgeMap)/255
        for i in range(img_size[0]):
            for j in range(img_size[1]):
                edgeMap[i, j] = edgeMap[i, j]/ratio

    # Convert output to uint8 type for displaying purposes
    edgeMap = numpy.array(edgeMap, dtype=numpy.uint8)

    # Display input and output image
    cv2.imshow("input", img)
    cv2.imshow("output", edgeMap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
