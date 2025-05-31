import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)  # Try 0 if 1 fails
detector = HandDetector(staticMode=False, maxHands=2)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=False)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # ASL "A" – All fingers down (fist)
        if fingers == [0, 0, 0, 0, 0]:
            cv2.putText(img, "A", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)

        # ASL "B" – All fingers up except thumb
        elif fingers == [0, 1, 1, 1, 1]:
            cv2.putText(img, "B", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)

        # ASL "C" – All fingers slightly curled (simulate by checking all fingers up)
        elif fingers == [1, 1, 1, 1, 1]:
            cv2.putText(img, "C", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)

        # ASL "D" – Only index finger up
        elif fingers == [0, 1, 0, 0, 0]:
            cv2.putText(img, "D", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 3)

        # ASL "E" – All fingers bent in with thumb under (simulate: all fingers down except thumb)
        elif fingers == [1, 0, 0, 0, 0]:
            cv2.putText(img, "E", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
    cv2.imshow("Hand Tracker", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


