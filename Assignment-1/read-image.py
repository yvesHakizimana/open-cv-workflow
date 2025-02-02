import cv2

# Read the required image
image = cv2.imread('assignment-001-given.jpg')
overlay = image.copy()

# Draw the green rectangle (unaffected by alpha blending)
cv2.rectangle(image, (265, 195), (988, 925), (0, 255, 0), 8)

# Create a mask for the black rectangle
mask = overlay.copy()
cv2.rectangle(mask, (820, 85), (1260, 190), (0, 0, 0), -1)  # Black rectangle on the mask

# Extract the region of interest (ROI) where blending should occur
roi = overlay[85:190, 820:1260]  # Y-range: 85 to 190, X-range: 820 to 1260
roi_blended = cv2.addWeighted(mask[85:190, 820:1260], 0.6, image[85:190, 820:1260], 0.6, 0)

# Replace the blended ROI back in the original image
image[85:190, 820:1260] = roi_blended

# Add the text on top of the blended black rectangle
cv2.putText(image, 'RAH972U', (820, 170), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 247, 82), 7,)

# Display the image in a new window
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the final image
cv2.imwrite('output.jpg', image)

# Close all OpenCV windows
cv2.destroyAllWindows()
