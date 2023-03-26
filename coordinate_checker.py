import cv2
import numpy as np

# Load the image
image = cv2.imread("b.jpg")

# Create a window to display the image
cv2.namedWindow("image")

# Define the mouse callback function
def mouse_callback(event, x, y, flags, param):
    # If left mouse button is clicked, save the coordinates of the point
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))

# Register the mouse callback function
cv2.setMouseCallback("image", mouse_callback)

# Display the image and wait for the user to select two points
points = []
while len(points) < 4:
    # Draw a red circle around the selected points
    for point in points:
        cv2.circle(image, point, 10, (0, 255, 0), -1)
    cv2.imshow("image", image)
    cv2.waitKey(1)

# Draw a red line between the two selected points
cv2.line(image, points[0], points[1], (0, 0, 255), 2)
cv2.line(image, points[3], points[2], (0, 0, 255), 2)

# Draw a red circle around the selected points
for point in points:
    cv2.circle(image, point, 10, (0, 255, 0), -1)

# Calculate the distance between the two points using Pythagoras' theorem
distance = np.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
distance1 = np.sqrt((points[3][0] - points[2][0])**2 + (points[3][1] - points[2][1])**2)

# Print the distance in pixels
print("Distance1 in pixels:", distance)
print("Distance2 in pixels:", distance1)

# Display the image with the selected points and line
cv2.imshow("image", image)
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
