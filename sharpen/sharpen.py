import sys
from PIL import Image
import numpy as np

assert(len(sys.argv) > 1), "Pass the name of the image as an argument"

""" works only for grayscale images """
""" edges are most visible in grayscale images """
def getNewPixelValue(im, pixel_y, pixel_x, kernel):
    pixel_val = 0

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if pixel_x + j < 0 or pixel_y + i < 0:
                continue
            if (max(pixel_x + j, im.shape[1] - 1) != pixel_x + j
                and max(pixel_y + i, im.shape[0] - 1) != pixel_y + i):
               pixel_val += im[pixel_y + i][pixel_x + j] * kernel[i + 1][j + 1]
    return max(pixel_val, 0)


im = Image.open(sys.argv[1])
im_matrix = np.asarray(im)
print(im_matrix.shape)

blurred_im = np.empty(im_matrix.shape)

for i in range(im_matrix.shape[0]):
    for j in range(im_matrix.shape[1]):
        blurred_im[i][j] = getNewPixelValue(im_matrix, i, j, [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        

output = Image.fromarray(np.uint8(blurred_im))
output.show()
output.save("output.jpg")
