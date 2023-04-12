import cv2
from pyzbar.pyzbar import decode

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    while True: # /shrug
        ret, img = cam.read()
        k = cv2.waitKey(1)
        if k%256 == 27:
            break
        elif k%256 == 32:
            barcode = decode(img)
            print(barcode)
            # later on I'll have the