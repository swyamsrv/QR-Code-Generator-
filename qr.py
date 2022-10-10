from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter
import pyqrcode
from datetime import datetime
import qrcode


class Quick:
    def __init__(self, root, link):
        self.root = root
        self.root.title("Your QR")
        self.root.geometry('525x525+460+215')
        self.root.maxsize(525, 525)
        self.root.wm_iconbitmap('qr-code-scan.ico')

        # BG IMAGE

        img = Image.open('qr_bg.jpg')
        img = img.resize((525, 525), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.bg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # frame

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=100, y=100, width=325, height=315)
        now = datetime.now()
        dat = now.strftime("%m_%d_%Y_%H_%M_%S")
        # qr_code.png("QR{}.png".format(dat), scale=4)
        # Image.open("QR{}.png".format(dat))
        # Creating a QRCode object of the size specified by the user
        qr = qrcode.QRCode(version=4,
                           box_size=10,
                           border=1)
        qr.add_data(link)  # Adding the data to be encoded to the QRCode object
        qr.make(fit=True)  # Making the entire QR Code space utilized
        img = qr.make_image()  # Generating the QR Code
        # fileDirec = loc.get() + '\\' + name.get()  # Getting the directory where the file has to be save
        img.save('QR{}.png'.format(dat))  # Saving the QR Code
        # Showing the pop up message on saving the file
        # messagebox.showinfo("DataFlair QR Code Generator", "QR Code is saved successfully!")

        img2 = Image.open('QR{}.png'.format(dat))
        img2 = img2.resize((310, 310), Image.Resampling.LANCZOS)
        self.qr2 = ImageTk.PhotoImage(img2)
        qr2 = Label(main_frame, image=self.qr2)
        qr2.place(x=0, y=0)

if __name__ == '__main__':
    root = Tk()
    obj = Quick(root)
    root.mainloop()