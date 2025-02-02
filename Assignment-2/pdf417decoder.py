import cv2
import numpy as np
import subprocess
import os
import platform

# Paths to required files (adjust as needed)
javase_jar = "javase-3.5.0.jar"
core_jar = "core-3.5.0.jar"
jcommander_jar = "jcommander-1.82.jar"
barcode_image = "../data/image1.jpg"

# Validate required files
for file in [javase_jar, core_jar, jcommander_jar, barcode_image]:
    if not os.path.exists(file):
        print(f"Error: {file} not found!")
        exit(1)

# Java command setup (use correct classpath separator)
classpath_sep = ";" if platform.system() == "Windows" else ":"
java_command = [
    "java",
    "-cp",
    f"{javase_jar}{classpath_sep}{core_jar}{classpath_sep}{jcommander_jar}",
    "com.google.zxing.client.j2se.CommandLineRunner",
    barcode_image  # Use direct path without file://
]

# Run the Java command
try:
    result = subprocess.run(java_command, capture_output=True, text=True, check=True)
    output = result.stdout.strip()
except subprocess.CalledProcessError as e:
    print("Error during decoding:")
    print(e.stderr)
    exit(1)

# Parse output for points (look under "Result points:")
points = []
in_points_section = False
for line in output.splitlines():
    if line.strip().startswith("Result points:"):
        in_points_section = True
        continue
    if in_points_section and line.strip().startswith("Point"):
        coords = line.split(":")[1].strip().replace("(", "").replace(")", "")
        x, y = map(float, coords.split(","))
        points.append((int(x), int(y)))

# Handle 1D barcode (2 points) by creating a rectangle
if len(points) == 2:
    (x1, y1), (x2, y2) = points
    points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

# Draw polygon if we have enough points
if len(points) >= 2:
    image = cv2.imread(barcode_image)
    if image is None:
        print("Error: Unable to read the image!")
        exit(1)

    # Convert points to numpy array in correct shape
    points_array = np.array(points, dtype=np.int32).reshape((-1, 1, 2))

    # Draw polygon or line based on number of points
    if len(points) >= 4:
        cv2.polylines(image, [points_array], isClosed=True, color=(0, 255, 0), thickness=2)
    else:
        cv2.line(image, tuple(points[0]), tuple(points[1]), (0, 255, 0), thickness=2)

    # Save and show results
    annotated_image_path = "annotated_barcode.png"
    cv2.imwrite(annotated_image_path, image)
    print(f"Annotated image saved as {annotated_image_path}")
    cv2.imshow("Detected Barcode", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No bounding points detected.")
