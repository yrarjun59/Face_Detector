import  cv2
from random import randrange

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect faces in
# img = cv2.imread('pa.jpg')
# img = cv2.imread('download.jpg')
# img = cv2.imread('multiple.jpg')
# img = cv2.imread('multiple-1.jpg')


# select the video or camera to capture
# webcam = cv2.VideoCapture('pic-1.mp4')
webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)

# Iterate forever ove frames
while True:
    
    # Read the current frame
    successful_frame_red, frame =  webcam.read()

    # Must convert to greyScale
    greyscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect Faces
    face_cordinates = trained_face_data.detectMultiScale(greyscale_img)
 
    # Draw rectangle around the faces
    for (x,y,w,h) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256), randrange(256)),2)


    cv2.imshow('Yr Arjun Face Detector', frame)

    # this key allow any key to continue
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81  or key == 113:
        break

# Release the VideoCapture object
webcam.release()


"""
for image
# Detect Faces
face_cordinates = trained_face_data.detectMultiScale(greyscale_img)

# Draw rectangle around the faces
for (x,y,w,h) in face_cordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),randrange(256), randrange(256)),2)

print(face_cordinates)

# load window with title and image
cv2.imshow('Yr Arjun Face Detector', img)

# this key allow any key to continue
cv2.waitKey()
"""

print("Code Competed.....>")