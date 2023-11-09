import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('brain.tif', cv2.IMREAD_GRAYSCALE)

# Set the threshold value for the bright part
threshold = 200

# Apply intensity slicing to create a binary image
binary = np.where(img > threshold, 255, 0).astype(np.uint8)

# Count the number of white pixels in each row
white_pixels_row = np.sum(binary / 255, axis=1)

# Count the number of white pixels in each column
white_pixels_col = np.sum(binary / 255, axis=0)

# Plot the data in a 1-D array for row and column counts
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

ax[0].plot(white_pixels_row)
ax[0].set_xlabel('Row number')
ax[0].set_ylabel('Number of white pixels')
ax[0].set_title('Row-wise pixel counts')

ax[1].plot(white_pixels_col)
ax[1].set_xlabel('Column number')
ax[1].set_ylabel('Number of white pixels')
ax[1].set_title('Column-wise pixel counts')

plt.show()
