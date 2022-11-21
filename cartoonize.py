from cartooner import cartoonize
import cv2
import os
import time

input_file = './imgs/input/12.jpg'
output_file = './imgs/output/cartoonized12.jpg' # output image file name
image = cv2.imread(input_file)
output = cartoonize(image)
print(output.shape)
cv2.imwrite(output_file, output)
