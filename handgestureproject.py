import os
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# variables
width, height = 1280, 720
folderPath = "Presentation"

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images
pathImages = os.listdir(folderPath)
print(pathImages)

# variables
imgList = []
drawMode = False
imgNumber = 0
hs, ws = int(120 * 1), int(120 * 1)
gestureThreshold = 300
buttonPress = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationNumber = 0
annotationStart = False

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Import Images
    success, img = cap.read()
    img = cv2.flip(img, 1)  # 1 means horizontal ; 0 means vertical
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    if hands and buttonPress is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # Get index finger tip coordinates (landmark 8)
        indexFinger = lmList[8][0], lmList[8][1]  # Use raw coordinates without interpolation

        if cy <= gestureThreshold:  # if hand is at the height of the face
            annotationStart = False
            # gesture 1 - Left
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")
                if imgNumber > 0:
                    buttonPress = True
                    annotations = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    imgNumber -= 1

            # gesture 2 - Right
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                if imgNumber < len(pathImages) - 1:
                    buttonPress = True
                    annotations = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    imgNumber += 1

        # Gesture 3 - show pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotationStart = False

        # Gesture 4 - Draw pointer
        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            # Add current finger position to annotations
            annotations[annotationNumber].append(indexFinger)
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
        else:
            annotationStart = False

        # Gesture 5 - Erase
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                annotations.pop(-1)
                annotationNumber -= 1
                buttonPress = True
    else:
        annotationStart = False

    # Button Pressed iterations
    if buttonPress:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPress = False

    # Draw all annotations
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                # Draw line between consecutive points
                cv2.line(imgCurrent, annotations[i][j-1], annotations[i][j], (0, 0, 200), 12)

    # Adding webcam image on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


