import cv2

vidcap = cv2.VideoCapture('bipin.mp4')
# cap=cv2.VideoCapture(0)
vidcap.set(cv2.CAP_PROP_POS_MSEC,2000) 
     # just cue to 20 sec. position
success,image=vidcap.read()
    
   
if success:
    cv2.imwrite("frame2sec.jpg", image)     # save frame as JPEG file
    cv2.imshow("2sec",image)
    cv2.waitkey()
cv2.destroyAllWindows()
