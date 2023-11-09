import cv2

def detect_filled_percentage(image_path, threshold):
    # Load the image
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to obtain binary image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # Calculate the filled percentage
    filled_percentage = cv2.countNonZero(thresh) / (img.shape[0]*img.shape[1]) * 100
    # Print the filled percentage
    print("Filled Percentage:", filled_percentage, "%")
    # Check if the filled percentage is less than the threshold
    if filled_percentage < threshold:
        print("Bottle is not properly filled")
    else:
        print("Bottle is properly filled")

# Example usage
detect_filled_percentage("bottle1.jpg", 80)
