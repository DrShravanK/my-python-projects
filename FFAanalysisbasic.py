import numpy as np
import cv2
brightnessofframes=[]
p=input("name of video file(eg-dance.mp4): ")
video=cv2.VideoCapture(p)
fps=video.get(cv2.CAP_PROP_FPS)
frames=video.get(cv2.CAP_PROP_FRAME_COUNT)
print('Frames per second=',fps, "No of Frames=", frames)
frames=int(frames)
for i in range(1,frames):
    video.set(cv2.CAP_PROP_POS_FRAMES,i)
    ret, frame=video.read()
    frame = cv2.resize(frame,(0,0), fx=0.5,fy=0.5)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    value=np.sum(hsv[:,:,2])
    pxl=hsv.shape[0]*hsv.shape[1]
    ab= value/pxl
    rab= round(ab,2)
    brightnessofframes.append(rab)
    print(i,rab)
    brightest = max(brightnessofframes)
    if i == frames:
        break

index=brightnessofframes.index(brightest)
frameno=int(index)+1
video.set(cv2.CAP_PROP_POS_FRAMES,frameno)
ret, frame=video.read()
cv2.imshow("brightestimage",frame)
print("frame number",frameno,"brightness value",brightest)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('brightestframe4.png',frame)
