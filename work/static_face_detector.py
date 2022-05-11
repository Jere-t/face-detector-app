import cv2
from random import randrange

dir_file_path = '/Users/jmaret/com/pictet/python/face-detector-app/'

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(dir_file_path+'data/model/haarcascade_frontalface_default.xml')

# choose an image to detectt
#img = cv2.imread(dir_file_path+'data/img/face1.png')
img = cv2.imread(dir_file_path+'data/img/multi-face1.png')

# Must convert img in grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect face  ==> detectMultiScale : Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

"""
when only 1 face
(x, y, width, height) = face_coordinates[0]
"""

for (x, y, width, height) in face_coordinates:
    # add rectangle on img (on not the gray one that is use only for detect) rectangle(image, start_point, end_point, color, thickness)
    cv2.rectangle(img, (x, y), (x+width, y+height), (randrange(200), randrange(190, 256), randrange(256)), 2)

# show window with title (1st arg) and img (2nd arg)
cv2.imshow("Clever Programmer Face Detection", img)
# wait until a key is pressed. ==> so the last command stay open and the code do not go further and end
cv2.waitKey(0)






print("Code Completed") # if we reach this line ==> everything before has been run
