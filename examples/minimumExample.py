import numpy as np        # `pip install numpy`
import cv2                # `pip install opencv-python`
import leapuvc            #  Ensure leapuvc.py is in this folder

# Start the Leap Capture Thread
#cv2.waitKey(20000)
leap = leapuvc.leapImageThread()
leap.start()

# Capture images until 'q' is pressed
while((not (cv2.waitKey(1) & 0xFF == ord('q'))) and leap.running):
    newFrame, leftRightImage = leap.read()
    if(newFrame):
        # Display the raw frame
        cv2.imshow('Frame L', leftRightImage[0])
        cv2.imshow('Frame R', leftRightImage[1])

cv2.destroyAllWindows()
