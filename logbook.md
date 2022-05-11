# LOGBOOK
This app has been created by following this [*link*](https://youtu.be/XIrOM9oP3pA)
> why would I need a logbook?
## What it should do
1.  Get a base of face picture
2.  Make them all **black & white** ==> The algorithm need to be in gray scale to look at a face
3.  Train the algorithm to detect faces
---
## Technologies & Packages
- Python
- *python-opencv*
---
## Steps
1.  `pip install opencv-python`  or `pip install opencv-python-headless`
2.  Create first python file.
3.  We will use the a haarcascade model from this [link](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml). Downloaded and put in the data/model folder.
4.  With the model we can have the rectangle of face(s) on a picture and then we put it and the img
5.  Did the same work for webcam or a video (capture frame by frame and add the rectangle with the model)
---

## GIT Commit
1. INIT app
2. static detection 
3. live detection
