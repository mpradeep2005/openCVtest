import cv2 as cv

cap=cv.VideoCapture("E:/Movies/Python Tutorial .mp4")

def rescaleFrame(frame,scale=0.5):
    height=frame.shape[1]*scale
    width=frame.sha
while True:
    isTrue,frame=cap.read()
    cv.imshow("ni",frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyWindow("ni")