import cv2
import cvzone
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
        for hand in hands:
            try:
                x, y, w, h = hand['bbox']
                handType = hand['type']
                label = 'Right' if handType == 'Left' else 'Left'

                cv2.rectangle(img, (x, y), (x + w + 20, y + h + 20), (0, 0, 255), 3)
                cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                lList = hand.get('lList', [])
                if lList and all(len(pt) == 3 for pt in lList):
                    for i in range(len(lList) - 1):
                        u1, v1, _ = lList[i]
                        u2, v2, _ = lList[i + 1]
                        cv2.circle(img, (u1, v1), 5, (0, 255, 0), cv2.FILLED)
                        cv2.line(img, (u1, v1), (u2, v2), (255, 0, 0), 2)

                fingers = detector.fingersUp(hand)
                count = fingers.count(1)
                cv2.putText(img, f"{count} fingers up", (x - 30, y - 40),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            except Exception as e:
                print("Error processing hand:", e)
                continue

    cv2.imshow("Hand Tracker", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


