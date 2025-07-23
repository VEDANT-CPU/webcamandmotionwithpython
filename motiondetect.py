import cv2
import time
first_frame=None

video=cv2.VideoCapture(0)#if you have more than one camera to your computer one of those camera
#will have index 0 second camera would be 1 and so on

while True:
    check, frame = video.read()
    print(check)#check is a boolean
    print(frame)#frame is a numpy array

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #we need to blur the image to smooth it and to increase accuracy in calculation
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue #because now we need to get delta frame so skip the below part in 1st loop

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold",thresh_frame)
    user_key=cv2.waitKey(2)
    #To have a systematic stopping mechanism. assign waitkey to user_key then do following
    if user_key==ord('q'):
        break

video.release()#now i release my camera so that i could access my object.
cv2.destroyAllWindows()