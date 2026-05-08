import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Give camera time to adjust
time.sleep(2)

# Capture background
print("Capturing background...")
time.sleep(3)

for i in range(60):
    ret, background = cap.read()

background = np.flip(background, axis=1)
print("Background captured")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Dark Blue Range
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Masks
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

    mask = mask1 + mask2

    # Clean mask
    kernel = np.ones((9,9), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    mask = cv2.GaussianBlur(mask, (7,7), 0)

    # Inverse mask
    mask_inv = cv2.bitwise_not(mask)

    # Segment out cloth from frame
    res1 = cv2.bitwise_and(background, background, mask=mask)

    # Segment out non-cloth part from frame
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()