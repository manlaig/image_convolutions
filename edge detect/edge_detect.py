import sys
from PIL import Image
import numpy as np

assert(len(sys.argv) > 1), "Pass the name of the image as an argument"

"""
works only for grayscale images
edges are most visible in grayscale images
"""
def getNewPixelValue(im, pixel_y, pixel_x):
    horiz = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    vert = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    horiz_edge = 0
    vert_edge = 0

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            x = pixel_x + j
            y = pixel_y + i
            if x >= 0 and y >= 0 and x <= im.shape[1] - 1 and y <= im.shape[0] - 1:
               horiz_edge += im[y][x] * horiz[i + 1][j + 1]
               vert_edge += im[y][x] * vert[i + 1][j + 1]
    newVal = abs(horiz_edge + vert_edge) / 2
    return newVal if newVal <= 255 else 255


im = Image.open(sys.argv[1])
im_matrix = np.asarray(im)
print(im_matrix.shape)

blurred_im = np.empty(im_matrix.shape)

for i in range(im_matrix.shape[0]):
    for j in range(im_matrix.shape[1]):
        blurred_im[i][j] = getNewPixelValue(im_matrix, i, j)

output = Image.fromarray(np.uint8(blurred_im))
output.show()
output.save("output.jpg")
