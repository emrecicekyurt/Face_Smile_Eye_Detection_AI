import cv2


# Taking the data that is xml file provided by opencv
faceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileData = cv2.CascadeClassifier('haarcascade_smile.xml')
# Using webcam
webcam = cv2.VideoCapture(0)

while True:
    success, img = webcam.read()

    # The image must be converted to white and black since the computer detects properly in this manner
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting the faces by using detectMultiScale
    face_cr = faceData.detectMultiScale(grayImg)

    # Create rectangle around of the faces detected. Coordinates come from face_cr obj
    for (x, y, w, h) in face_cr:
        cv2.rectangle(img, (x, y), (x+w,y+h+30), (255,0,255), 3)
        face_frame = img[y:y+h, x:x+w]
        grayFace = cv2.cvtColor(face_frame, cv2.COLOR_BGR2GRAY)
        # Detecting the smiles in face by using detectMultiScale
        smile_cr = smileData.detectMultiScale(grayFace,scaleFactor=1.7, minNeighbors=20)

        for(a, b, c, d) in smile_cr:
            # Drawing rectangles around smile
            cv2.rectangle(face_frame, (a, b), (a+c, b+d), (0,255,0), 2)
            # Putting smiling text under the frame
            if len(smile_cr)>0:
                cv2.putText(img, "Smiling", (x, y+h+70), fontScale=1, fontFace=cv2.FONT_ITALIC, color=(0,255,0), thickness=3)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break