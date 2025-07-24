import cv2
from datetime import datetime
first_frame=None
status_list=[None,None]#python would give out of range error because it tries to access from
#list when its empty in line 40 so do this to avoid error.
times=[]

video=cv2.VideoCapture(0)#if you have more than one camera to your computer one of those camera
#will have index 0 second camera would be 1 and so on

while True:
    check, frame = video.read()
    status=0 #assuming no motion in current frame at the moment webcam starts.
    #print(check)check is a boolean
    #print(frame)frame is a numpy array

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #we need to blur the image to smooth it and to increase accuracy in calculation
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue #because now we need to get delta frame so skip the below part in 1st loop
    
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    #to remove little black holes from white areas, we smoothen them.
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    #contour detection of white bodies in threshold frame.
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #to keep contours enclosing areas bigger than a criteria
    for contours in cnts:
        if cv2.contourArea(contours) < 1000:
            continue
        status=1 #when python finds contour with big enough area set status to 1.
        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    status_list.append(status)
    #we put if below as we want to check transition after latest status appended.
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold",thresh_frame)
    cv2.imshow("ColorFrame",frame)

    user_key=cv2.waitKey(2)
    #To have a systematic stopping mechanism. assign waitkey to user_key then do following
    if user_key==ord('q'):
        if status==1:
            times.append(datetime.now())#when q is pressed while object moving in frame
            #you want the time of pressing q as endtime.
        break
    #print(status) to print 1 or 0 depending on if motion in camera or not respectively.

print(status_list)
print(times)
video.release()#now i release my camera so that i could access my object.
cv2.destroyAllWindows()