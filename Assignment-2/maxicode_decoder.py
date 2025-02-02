import cv2
from pyzxing import BarCodeReader

image = cv2.imread('../data/image6.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite('processed_maxicode.png', thresh)
reader = BarCodeReader()
result = reader.decode('processed_maxicode.png')[0]['raw']

print(result)
