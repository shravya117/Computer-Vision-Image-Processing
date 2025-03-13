import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = 'logo.png'  
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
#Gx = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
#Gy = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
G = np.sqrt(Gx**2 + Gy**2)
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
edges = cv2.Canny(blurred_image, 100, 200)
#Gx = np.uint8(255 * np.abs(Gx) / np.max(Gx))
#Gy = np.uint8(255 * np.abs(Gy) / np.max(Gy))
G = np.uint8(255 * G / np.max(G))
laplacian_abs = cv2.convertScaleAbs(laplacian)
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(Gx, cmap='gray')
plt.title('Gradient in X direction')
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(Gy, cmap='gray')
plt.title('Gradient in Y direction')
plt.axis('off')

# Edge-detected image
#Sobel Edge Detection
plt.subplot(2, 2, 4)
plt.imshow(G, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

#Laplacian Edge Detection
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 2)
plt.imshow(laplacian_abs, cmap='gray')
plt.title('Laplacian Edge Detection')
plt.axis('off')

#Canny Edge Detection
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

plt.show()


