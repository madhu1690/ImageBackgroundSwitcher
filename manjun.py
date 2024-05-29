import cv2
import numpy as np

# Load the images
img = cv2.imread(r"C:\Users\s\OneDrive\Desktop\manjunath\pic 1.png")
bg = cv2.imread(r"C:\Users\s\OneDrive\Desktop\manjunath\pic 2.jpg")

# Resize the background to match the size of the original image
bg = cv2.resize(bg, (img.shape[1], img.shape[0]))

# Convert the images to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold the HSV image to isolate the green screen
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert the mask to get the foreground
mask_inv = cv2.bitwise_not(mask)

# Mask the original image to get the foreground
fg = cv2.bitwise_and(img, img, mask=mask_inv)

# Mask the background image to get the background where the green screen was
bg_masked = cv2.bitwise_and(bg, bg, mask=mask)

# Combine the foreground and background
result = cv2.add(fg, bg_masked)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Masked Image', fg)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

