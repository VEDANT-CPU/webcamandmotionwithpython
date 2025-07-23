import cv2
import time

video=cv2.VideoCapture(0)#if you have more than one camera to your computer one of those camera
#will have index 0 second camera would be 1 and so on

while True:
    check, frame = video.read()
    print(check)#check is a boolean
    print(frame)#frame is a numpy array

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Captured Video",gray)
    user_key=cv2.waitKey(2)
    #To have a systematic stopping mechanism. assign waitkey to user_key then do following
    if user_key==ord('q'):
        break

video.release()#now i release my camera so that i could access my object.
cv2.destroyAllWindows()