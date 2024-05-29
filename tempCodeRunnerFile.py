import cv2
import numpy as np

# Load the images
img = cv2.imread(r"C:\Users\s\OneDrive\Desktop\manjunath\pic 1.jpg")
bg = cv2.imread(r"C:\Users\s\OneDrive\Desktop\manjunath\pic 2.jpg")

# Convert the images to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
bg_hsv = cv2.cvtColor(bg, cv2.COLOR_BGR2HSV)

# Threshold the HSV images to isolate the green screen
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

# Apply the mask to the original image
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Replace the green screen with the background image
result = cv2.bitwise_or(masked_img, bg)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Masked Image', masked_img)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
