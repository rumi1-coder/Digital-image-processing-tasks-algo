import cv2
import matplotlib.pyplot as plt

def count_intensity_values(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Create a dictionary to store intensity counts
    intensity_counts = {}

    # Iterate over each pixel in the image
    for row in image:
        for pixel in row:
            # Get the intensity value of the pixel
            intensity = int(pixel)

            # If the intensity value is not already in the dictionary, add it with count 1
            if intensity not in intensity_counts:
                intensity_counts[intensity] = 1
            # If the intensity value is already in the dictionary, increment its count by 1
            else:
                intensity_counts[intensity] += 1

    return intensity_counts

# Example usage
image_path = "grain3.tif"
intensity_counts = count_intensity_values(image_path)
print(intensity_counts)

# Plot the intensity values using matplotlib
plt.bar(intensity_counts.keys(), intensity_counts.values())
plt.xlabel("Intensity value")
plt.ylabel("Count")
plt.show()
