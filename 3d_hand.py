from cvzone.HandTrackingModule import HandDetector
import cv2
import socket

from matplotlib import image


cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(5,480)



success,img=cap.read()
h,w,_=img.shape
detector=HandDetector(detectionCon=0.8, maxHands=2)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddressPort=('127.0.0.1',5052)


while True:
    # Get image frame
    success,img=cap.read()
    # Find hands and landmarks
    hands,img=detector.findHands(img) # with Draw
    #hands=detector.findhands(img,draw=False)   #without Draw
    data=[]


    if hands:

        # Hand 1
        hand=hands[0]
        lmList=hand['lmList']    #list of 21 landmark points
        for lm in lmList:
            data.extend([lm[0],h-lm[1],lm[2]])
        


        sock.sendto(str.encode(str(data)),serverAddressPort)
    


    #cv2.imshow('Image',cv2.flip(img, 1))
    cv2.imshow('Image',img)
    cv2.waitKey(1)