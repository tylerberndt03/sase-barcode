import cv2
import gspread
#from pyzbar.pyzbar import decode
import zxingcpp

if __name__ == "__main__":
    # eventSheetN = input("Event Sheet Name:")

    # gc = gspread.service_account() # This will connect to a set drive or something
    # memberSheet = gc.open("Members").get_worksheet(0) # or whatever it's called
    # eventSheet = gc.open(eventSheetN).get_worksheet(0)

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("img")

    while True: # /shrug
        ret, img = cam.read()
        cv2.imshow("img", img)
        k = cv2.waitKey(1)
        if k%256 == 27:
            break
        elif k%256 == 32:
            barcode = zxingcpp.read_barcodes(img)
            print(barcode)
            # later on I'll have the
        #barcode = input("Test barcode:")
        # try:
        #     row = memberSheet.col_values(1).index(barcode) + 1
        # except ValueError:
        #     print("No info found")
        # else:
        #     member = memberSheet.row_values(row)
        #     print("Info found: " + member[1])
        #     eventSheet.append_row(member)