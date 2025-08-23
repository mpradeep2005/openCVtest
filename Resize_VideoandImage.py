import cv2 as cv


cap=cv.VideoCapture("E:/Movies/Python Tutorial .mp4")

def rescaleFrame(frame,scale=0.5):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimension=(height,width)
    return  cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

while True:
    isTrue,frame=cap.read()
    cv.imshow("Original",frame)
    frame_reduced=rescaleFrame(frame)
    cv.imshow("Rescaled",frame_reduced)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()