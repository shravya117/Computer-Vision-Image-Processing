import numpy as np
import cv2 as cv

#Rotation
img = cv.imread('rotation.jpg') 
if img is None:
    print("Error: Unable to load image 'rotation.jpg'")
else:
    rows, cols = img.shape[:2] 
    img_rotation = cv.warpAffine(img,
                                cv.getRotationMatrix2D((cols/2, rows/2), 30, 0.6),  
                                (cols, rows))  
    
    cv.imshow('Rotated Image', img_rotation) 
    cv.imwrite('rotation_out.jpg', img_rotation) 
    cv.waitKey(0)
    cv.destroyAllWindows()

#Scaling
img = cv.imread('scaling.jpg')  
if img is None:
    print("Error: Unable to load image 'scaling.jpg'")
else:
    img_scaled = cv.resize(img, (250, 200), interpolation=cv.INTER_AREA)
    cv.imshow('Scaled Image', img_scaled)
    cv.imwrite('scaling_out.jpg', img_scaled)
    cv.waitKey(0)
    cv.destroyAllWindows()

#Translation
import numpy as np
import cv2 as cv
img = cv.imread('translation.jpg')
if img is None:
    print("Error: Unable to load image 'translation.jpg'")
else:
    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 50]])  
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.imshow('Translated Image', dst)
    cv.imwrite('translation_out.jpg', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


