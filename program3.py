import cv2
<<<<<<< HEAD
import numpy as np

# Load the image
image_path = "logo.png"  # Replace with the path to your image
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection using Canny
edges = cv2.Canny(gray, 100, 200)

# Texture extraction using an averaging filter
kernel = np.ones((5, 5), np.float32) / 25
texture = cv2.filter2D(gray, -1, kernel)

# Display the original image, edges, and texture
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Texture", texture)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
=======
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
>>>>>>> 821833f6c64df709aaeb819f1e1d8c91dd36b596
