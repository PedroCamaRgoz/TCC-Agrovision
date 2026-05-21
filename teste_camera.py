import cv2

camera = cv2.VideoCapture(0, cv2.CAP_MSMF)

while True:
    sucesso, frame = camera.read()

    if sucesso:
        cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()