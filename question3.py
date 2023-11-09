import cv2
import numpy as np

# Load the image
img = cv2.imread('grain3.tif')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the basic log transformation with c = 1
c = 1
log_transformed = c * np.log10(1 + gray)
log_transformed = cv2.normalize(log_transformed.astype(np.uint8), None, 0, 255, cv2.NORM_MINMAX)

# Display the result
cv2.imshow('Basic log transformation, c=1', log_transformed)
cv2.waitKey(0)

# Apply the inverse log transformation with c = 1
c = 1
inverse_log_transformed = c * (1 - np.exp(-gray))
inverse_log_transformed = cv2.normalize(inverse_log_transformed.astype(np.uint8), None, 0, 255, cv2.NORM_MINMAX)

# Display the result
cv2.imshow('Inverse log transformation, c=1', inverse_log_transformed)
cv2.waitKey(0)

# Apply the square root transformation with c = 1
c = 1
sqrt_transformed = c * np.sqrt(gray)
sqrt_transformed = cv2.normalize(sqrt_transformed.astype(np.uint8), None, 0, 255, cv2.NORM_MINMAX)

# Display the result
cv2.imshow('Square root transformation, c=1', sqrt_transformed)
cv2.waitKey(0)

cv2.destroyAllWindows()
