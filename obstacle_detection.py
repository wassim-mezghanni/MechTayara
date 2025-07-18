import cv2

OBSTACLE_THRESHOLD = 350

def detect_obstacle(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresholded = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(thresholded, 30, 100)
    h, w = edges.shape
    roi = edges[h//3:2*h//3, w//3:2*w//3]
    non_zero_count = cv2.countNonZero(roi)
    return non_zero_count > OBSTACLE_THRESHOLD