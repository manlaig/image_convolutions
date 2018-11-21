import sys
from PIL import Image
import numpy as np

assert(len(sys.argv) > 1), "Pass the name of the image as an argument"


def getBlurValue(im, pixel_y, pixel_x, channel, kernel_size=3):
    # 5 by 5 kernel
    if kernel_size == 5:
        kernel = [[1,4,7,4,1], [4,16,26,16,4], [7,26,41,26,7], [1,4,7,4,1], [4,16,26,16,4]]
    else:
        kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]

    pixel_blur = 0
    offset = int(kernel_size/2)

    for i in range(-offset, offset+1, 1):
        for j in range(-offset, offset+1, 1):
            if pixel_x + j < 0 or pixel_y + i < 0:
                continue
            if (max(pixel_x + j, im.shape[1] - 1) != pixel_x + j
                and max(pixel_y + i, im.shape[0] - 1) != pixel_y + i):
               pixel_blur += im[pixel_y + i][pixel_x + j][channel] * kernel[i + offset][j + offset]
    
    pixel_blur /= 273 if kernel_size == 5 else 16
    return pixel_blur


im = Image.open(sys.argv[1])
im_matrix = np.asarray(im)
print(im_matrix.shape)

blurred_im = np.empty(im_matrix.shape)

for i in range(im_matrix.shape[0]):
    for j in range(im_matrix.shape[1]):
        for k in range(im_matrix.shape[2]):
            blurred_im[i][j][k] = getBlurValue(im_matrix, i, j, k, 3)

output = Image.fromarray(np.uint8(blurred_im))
output.show()
output.save("output.jpg")
