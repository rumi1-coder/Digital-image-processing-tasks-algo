import cv2
import numpy as np

# Define custom box filters of sizes 7x7 and 3x3
kernel_7 = np.ones((7, 7), np.float32) / 49
kernel_3 = np.ones((3, 3), np.float32) / 9

# Load the input image
img = cv2.imread("grain3.tif", cv2.IMREAD_GRAYSCALE)

# Apply the custom box filters to the image
O7 = cv2.filter2D(img, -1, kernel_7)
O3 = cv2.filter2D(img, -1, kernel_3)

# Calculate the final output image
final_output = img - np.abs(O7 - O3)

# Display the resulting image
cv2.imshow("Output Image", final_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
