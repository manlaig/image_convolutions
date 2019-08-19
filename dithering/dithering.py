"""
This the implementation of Floyd-Steinberg dithering algorithm
NOTE: only use with grayscale images
"""

import sys
from PIL import Image
import numpy as np

assert(len(sys.argv) > 1), "Pass the name of the image as an argument"

im = Image.open(sys.argv[1])
im_matrix = np.asarray(im)
threshholded = np.empty(im_matrix.shape)

possible_colors = 3

for i in range(im_matrix.shape[0]):
    for j in range(im_matrix.shape[1]):
            threshholded[i][j] = round(im_matrix[i][j] / 255. * possible_colors) * 255. / possible_colors

for i in range(1,len(threshholded)-1,1):
    for j in range(1,len(threshholded[i])-1,1):
        if(threshholded[i][j] > 255):
            threshholded[i][j] = 255
        elif(threshholded[i][j] < 0):
            threshholded[i][j] = 0

        diff = im_matrix[i][j] - threshholded[i][j]
        threshholded[i][j+1] += diff * 7 / 16
        threshholded[i+1][j-1] += diff * 3 / 16
        threshholded[i+1][j] += diff * 5 / 16
        threshholded[i+1][j+1] += diff * 1 / 16

output = Image.fromarray(np.uint8(threshholded))
output.show()
output.save("output.jpg")
