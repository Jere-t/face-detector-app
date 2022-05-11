import cv2

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(../data/model/haarcascade_frontalface_default.xml)

# choose an image to detectt
img = cv2.imread(../data/img/face1.png)

# Must convert img in grayscale
grayscaled_img = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect face  ==> detectMultiScale : Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)




# show window with title (1st arg) and img (2nd arg)
cv2.imshow("Clever Programmer Face Detection", grayscaled_img)
# wait until a key is pressed. ==> so the last command stay open and the code do not go further and end
cv2.waitKey()






print("Code Completed") # if we reach this line ==> everything before has been run
