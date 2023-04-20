import cv2
import gspread
#from pyzbar.pyzbar import decode
import zxingcpp
import tkinter as tk

# ret, img = cam.read()
#         #cv2.imshow("img", img)
#         k = cv2.waitKey(1)
#         if k%256 == 27:
#            break
#         elif k%256 == 32:
#            barcode = zxingcpp.read_barcodes(img)
#            print(barcode)
#             later on I'll have the
           
def scanBarcode():
        ret, img = cam.read()
        #cv2.imshow("img", img)
        barcode = zxingcpp.read_barcodes(img)
        print(barcode)
        barcode = getBarcode.get()
        try:
            row = memberSheet.col_values(1).index(barcode) + 1
        except ValueError:
            print("No info found")
            status.set(barcode + ":\nNo info found")
        else:
            member = memberSheet.row_values(row)
            print("Info found: " + member[1])
            status.set(":\nInfo found: " + member[1])
            eventSheet.append_row(member)

if __name__ == "__main__":
    eventSheetN = input("Event Sheet Name:")

    gc = gspread.service_account() # This will connect to a set drive or something
    memberSheet = gc.open("Members").get_worksheet(0) # or whatever it's called
    eventSheet = gc.open(eventSheetN).get_worksheet(0)

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("img")
    #Tescv2.imshow("img", img)

    window = tk.Tk()
    captureImg = tk.Button(text="Scan", command=scanBarcode)
    status = tk.StringVar(value="Waiting")
    statusLabel = tk.Label(textvariable=status)
    captureImg.pack()
    statusLabel.pack()

    getBarcode = tk.Entry()
    getBarcode.pack()

    window.mainloop()



    # while True: # /shrug
    #     #ret, img = cam.read()
    #     #cv2.imshow("img", img)
    #     #k = cv2.waitKey(1)
    #     #if k%256 == 27:
    #     #    break
    #     #elif k%256 == 32:
    #     #    barcode = zxingcpp.read_barcodes(img)
    #     #    print(barcode)
    #         # later on I'll have the
    #     barcode = getBarcode.get()
    #     try:
    #         row = memberSheet.col_values(1).index(barcode) + 1
    #     except ValueError:
    #         print("No info found")
    #     else:
    #         member = memberSheet.row_values(row)
    #         print("Info found: " + member[1])
    #         eventSheet.append_row(member)