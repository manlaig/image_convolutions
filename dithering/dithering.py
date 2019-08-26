"""
This is the implementation of Floyd-Steinberg dithering algorithm
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
        for k in range(im_matrix.shape[2]):
            threshholded[i][j][k] = round(im_matrix[i][j][k] / 255. * possible_colors) * 255. / possible_colors

for i in range(im_matrix.shape[0]-1):
    for j in range(im_matrix.shape[1]-1):
        for k in range(im_matrix.shape[2]-1):
            if(threshholded[i][j][k] > 255):
                threshholded[i][j][k] = 255
            elif(threshholded[i][j][k] < 0):
                threshholded[i][j][k] = 0

            diff = im_matrix[i][j][k] - threshholded[i][j][k]
            threshholded[i][j+1][k] = int(diff * 7. / 16. + threshholded[i][j+1][k])
            threshholded[i+1][j-1][k] = int(diff * 3. / 16. + threshholded[i+1][j-1][k])
            threshholded[i+1][j][k] = int(diff * 5. / 16. + threshholded[i+1][j][k])
            threshholded[i+1][j+1][k] = int(diff * 1. / 16. + threshholded[i+1][j+1][k])

output = Image.fromarray(np.uint8(threshholded))
output.show()
output.save("output.jpg")
