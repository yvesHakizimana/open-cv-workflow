# README: Barcode & Aztec Code Decoder

## Overview

This project provides Python scripts for decoding barcodes and Aztec codes from images. It utilizes **OpenCV** for image processing and **pyzbar**/**pyzxing** for barcode recognition. The scripts can detect and extract barcode data, highlight barcode locations, and annotate the detected barcodes within images.

## Features

- Decode multiple barcode types, including QR codes, Aztec codes, and MaxiCodes.
- Apply preprocessing techniques (grayscale conversion and thresholding) to enhance barcode readability.
- Highlight detected barcodes using OpenCV drawing functions.
- Save annotated images with barcode locations and decoded data.

## Dependencies

Ensure you have the following dependencies installed:

```bash
pip install opencv-python pyzbar pyzxing numpy
```

## Scripts & Functionality

### 1. **Barcode Reader using `pyzxing`**

- Reads an image, converts it to grayscale, and applies binary thresholding.
- Saves the processed image.
- Uses `BarCodeReader` from `pyzxing` to decode the barcode.
- Prints the extracted barcode data.

**Usage:**

```python
import cv2
from pyzxing import BarCodeReader

image = cv2.imread('../data/image5.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite('processed_image.png', thresh)

reader = BarCodeReader()
result = reader.decode('processed_image.png')[0]['raw']

print(result)
```

### 2. **Aztec Code Decoder using `pyzbar`**

- Reads an image containing a barcode or Aztec code.
- Decodes the barcode using `pyzbar.decode()`.
- Draws a bounding box around the detected barcode.
- Annotates the barcode with the decoded data.
- Displays the processed image and saves it.

**Usage:**

```python
from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image
image = cv2.imread("../data/image4.jpg")

# Decode the barcode
barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Barcode Data: {data}")

    points = barcode.polygon
    points = [(point.x, point.y) for point in points]
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

    # Annotate the decoded data beside the bounding box
    x, y = points[0]
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Display the image with the barcode highlighted and annotated
cv2.imshow("Barcode with Annotation", image)
cv2.waitKey(0)

# Save the annotated image
output_file = "results/decoded_barcode.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")

cv2.destroyAllWindows()
```

### 3. **MaxiCode Decoder using `pyzxing`**

- Converts an image to grayscale and applies thresholding.
- Uses `BarCodeReader` to decode MaxiCodes.
- Prints the decoded information.

**Usage:**

```python
import cv2
from pyzxing import BarCodeReader

image = cv2.imread('../data/image6.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite('processed_maxicode.png', thresh)
reader = BarCodeReader()
result = reader.decode('processed_maxicode.png')[0]['raw']

print(result)
```

## How to Run

1. Place the input image inside the `data` folder.
2. Run any script with:

   ```bash
   python script_name.py
   ```

3. If using the GUI mode, press any key to close the image window.
4. The annotated barcode images will be saved in the `results` folder.

## Output

- The scripts will display the detected barcode in an image window.
- The decoded barcode data is printed in the terminal.
- Processed images with bounding boxes and annotations are saved.

## Notes

- Ensure the input images have good resolution for better decoding accuracy.
- The thresholding step can be adjusted if decoding fails.
- If the barcode is not detected, check for image distortions or lighting issues.
