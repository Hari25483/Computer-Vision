import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Define the radius and thickness of the circle
radius = 5
thickness = 2

# Create a window to display the image
cv2.namedWindow("image")

# Define the mouse callback function
def mouse_callback(event, x, y, flags, param):
    # If left mouse button is clicked, save the coordinates of the point
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 2:
            points.append((x, y))

    # Draw a circle around the clicked point
    if len(points) == 1:
        cv2.circle(image, points[0], radius, (0, 0, 255), thickness)

    if len(points) == 2:
        cv2.circle(image, points[1], radius, (0, 0, 255), thickness)
        # Calculate the distance between the two points using Pythagoras' theorem
        distance = np.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
        # Print the distance in pixels
        print("Distance in pixels:", distance)

# Register the mouse callback function
cv2.setMouseCallback("image", mouse_callback)

# Display the image and wait for the user to select two points
points = []
while len(points) < 2:
    cv2.imshow("image", image)
    cv2.waitKey(1)

# Close the window
cv2.destroyAllWindows()
