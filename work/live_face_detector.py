import cv2

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('data/model/haarcascade_frontalface_default.xml')

# capture video from webcam if you type '0'
webcam = cv2.VideoCapture(0)

#to capture a video ==> webcam = cv2.VideoCapture('path/to/video')

print("Press Q to quit")

# Iterate forever over frames
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, width, height) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)

    cv2.imshow("Clever Programmer Face Detection", frame)
    # wait 1 milli second
    key = cv2.waitKey(1)

    # Quit the loop by press q key
    if key == 81 or key == 113:
        break
# End of the infinite loop

# Release videocapture obj
webcam.release()

print("Code Completed") # if we reach this line ==> everything before has been run
