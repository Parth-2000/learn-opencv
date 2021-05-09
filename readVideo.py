import cv2 as cv

capture = cv.VideoCapture(0)
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# output = cv.VideoWriter('test.avi', fourcc, 20.0, (640, 480))

print(capture.get(cv.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

capture.set(3, 1280)
capture.set(4, 720)

print(capture.get(3))
print(capture.get(4))

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # output.write(frame)
        cv.imshow("Frame", gray)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
# output.release()
cv.destroyAllWindows()
