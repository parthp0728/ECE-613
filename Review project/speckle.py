

from PIL import Image  
import PIL
from os import walk
import sys
import os

import numpy as np
import cv2
import random

def sp_noise(image,prob):
	row,col,ch = image.shape
	gauss = np.random.randn(row,col,ch)
	gauss = gauss.reshape(row,col,ch)        
	noisy = image + image * gauss
	return noisy

init_path = "E:/sem-7/minor/dataset/maps/clean_train" + "/"
dest_path = "E:/sem-7/minor/dataset/maps/gpu_train"  + "/"
print(os.getcwd())
for (dirpath, dirnames, filenames) in walk(init_path):
	print(os.getcwd())
	for data_file in filenames:
		# print(os.getcwd())
		print(data_file)
		image = cv2.imread(init_path+data_file,cv2.CV_LOAD_IMAGE_GRAYSCALE)
		# print(image) # Only for grayscale image
		noise_img = sp_noise(image,0.05)
		cv2.imwrite(dest_path+data_file, noise_img)
  


