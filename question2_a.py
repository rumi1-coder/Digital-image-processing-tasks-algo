import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('brain.tif', cv2.IMREAD_UNCHANGED)

# Convert the image to grayscale if it has multiple channels
if len(img.shape) > 2:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set the threshold value for the bright part
threshold = 200

# Apply intensity slicing to create a binary image
binary = np.where(img > threshold, 255, 0).astype(np.uint8)

# Display the original image, binary image, and side-by-side comparison
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))

ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original Image')

ax[1].imshow(binary, cmap='gray')
ax[1].set_title('Binary Image')

ax[2].imshow(img, cmap='gray')
ax[2].imshow(binary, alpha=0.4, cmap='Reds')
ax[2].set_title('Original and Binary Image')




plt.show()
