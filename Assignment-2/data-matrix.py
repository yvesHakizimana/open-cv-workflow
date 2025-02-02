import pyzxing

reader = pyzxing.BarCodeReader()

barcode = reader.decode('../data/image2.jpg')

if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No Data Matrix code found.")
