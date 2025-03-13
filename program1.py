import cv2
import numpy as np

def split_image_into_squares(image_path, num_of_squares):
    image = cv2.imread(image_path)
    min_dim = min(image.shape[:2])
    step = min_dim // num_of_squares
    
    squares = [image[i:i+step, j:j+step] for i in range(0, min_dim, step) for j in range(0, min_dim, step)]
    return squares

squares = split_image_into_squares('image2.jpg', 2)
for idx, square in enumerate(squares):
    cv2.imwrite(f'img_{idx}.jpg', square)  