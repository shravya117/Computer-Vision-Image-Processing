import cv2
img = cv2.imread('image1.jpg')
h, w, channels = img.shape
half = w//2
half2 = h//2
top = img[:half2, :half]
bottom = img[half2:, :half]
left_part = img[:half2, :half] 
right_part = img[:half2, half:] 
cv2.imshow('Left part', left_part)
cv2.imshow('Right part', right_part)

cv2.imshow('Top', top)
cv2.imshow('Bottom', bottom)
cv2.imwrite('top.jpg', top)
cv2.imwrite('bottom.jpg', bottom)
cv2.imwrite('right.jpg', right_part)
cv2.imwrite('left.jpg', left_part)
cv2.waitKey(0)
