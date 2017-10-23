import cv2
import numpy as np
import sys
import os
import glob
from pathlib import Path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Rainbow trout-steelhead/*.jpg")
filelist = glob.glob('**/*.jpg',recursive=True)
string = 0;
for file in filelist:
	try:
		img = cv2.imread(file, 1) # scrolls through all the fish images as of late.
		small = cv2.resize(img, (400,250)) #changes images into a 400px by 250px size.
		small = cv2.cvtColor(small, cv2.COLOR_BGR2Lab) #possible color change for cvtColor
		cv2.imwrite(string++,small)
		cv2.imshow('Fish filter img',small)
		cv2.waitKey(0)
		cv2.destroyAllWindows
	except IOError as exc:
		if exc.errno != errno.EISDIR:
			raise

