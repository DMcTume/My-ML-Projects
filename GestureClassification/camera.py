import cv2

video = cv2.VideoCapture(0)
video.set(3, 500)
video.set(4, 500)

while(True):
    ret, frame = video.read()
    cv2.imshow("frame", frame)

    print(ret)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()


