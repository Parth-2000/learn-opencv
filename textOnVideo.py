import cv2 as cv
import datetime

cap = cv.VideoCapture(0)

# cap.set(3, 3000)
# cap.set(4, 3000)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        font = cv.FONT_HERSHEY_SIMPLEX
        # text = "Width: " + str(cap.get(3)) + " Height: " + str(cap.get(4))
        date = str(datetime.datetime.now())
        frame = cv.putText(frame, date, (30, 30), font, 1, (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

