import os
#import cv2
import numpy
import os
import csv

path = 'Attendance.csv'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, path)
#myList = os.listdir(path)
#print (STATIC_ROOT)

with open('Attendance.csv' , 'r+') as f:
	myDataList = f.read()
	print(myDataList)
