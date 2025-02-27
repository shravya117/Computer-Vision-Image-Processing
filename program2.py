import cv2
img = cv2.imread('image3.jpg')
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
left1 = img[:, :width_cutoff]
right1 = img[:, width_cutoff:]
img = cv2.rotate(left1, cv2.ROTATE_90_CLOCKWISE)
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
l1 = img[:, :width_cutoff]
l2 = img[:, width_cutoff:]
l1 = cv2.rotate(l1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("top_left.jpg", l1)
l2 = cv2.rotate(l2, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("bottom_left.jpg", l2)
img = cv2.rotate(right1, cv2.ROTATE_90_CLOCKWISE)
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
r1 = img[:, :width_cutoff]
r2 = img[:, width_cutoff:]
r1 = cv2.rotate(r1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("top_right.jpg", r1)
r2 = cv2.rotate(r2, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("bottom_right.jpg", r2)