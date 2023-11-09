import cv2
import numpy as np

def separate_teeth(image_path):
    # Load the image as grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply adaptive thresholding to enhance the contrast between teeth and background
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 5)

    # Apply morphological operations to remove small objects and smooth the contours
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Find the contours of the objects in the image
    contours, hierarchy = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours of the objects on a new blank image
    blank = np.zeros_like(img)
    cv2.drawContours(blank, contours, -1, (255, 255, 255), -1)

    # Apply binary thresholding to isolate the teeth
    ret, teeth = cv2.threshold(blank, 0, 255, cv2.THRESH_BINARY)

    return teeth

# Example usage
image_path = 'dental_xray.tif'
teeth = separate_teeth('dental_xray.tif')
cv2.imshow('Teeth', teeth)
cv2.waitKey(0)
