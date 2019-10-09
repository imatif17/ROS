import numpy as np
import sys
#import argparse
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2


def left_right():
	lower_red = np.array([170,87,111])
	upper_red = np.array([180, 255, 255])

	cam = cv2.VideoCapture(0)
	ret,frame = cam.read()
	if(ret):
		frame = cv2.flip(frame,1)
		frame = cv2.resize(frame,(1000,1000))
		(height,width,_) = frame.shape
		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		hsv = cv2.dilate(hsv,np.ones((7,7)))
		mask = cv2.inRange(hsv,lower_red,upper_red)
		contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		if contours:
			largest_contour = max(contours, key = cv2.contourArea)
			x,y,w,h = cv2.boundingRect(largest_contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
			frame = cv2.drawContours(frame, largest_contour, -1, (255,255,0), 3)
			centre = x+(w/2)
			if(centre < width/2):
				return 'left'
			else:
				return 'right'
		return 'No object'
			
		#cv2.imshow('red colour detection',frame)
		cam.release()
		cv2.destroyAllWindows()
        

