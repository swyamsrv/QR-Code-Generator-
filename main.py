# Generate a QR code = Quick Response code
from qr import Quick
import pyqrcode  # The pyqrcode module is a QR code generator that is simple to use and written in pure python.
# The module automates most of the building process for you. Generally, QR codes can be created using this library
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter


class QR:
    def __init__(self, root):
        self.root = root
        self.root.title("Your QR Generator")
        self.root.geometry('525x300+460+215')
        self.root.maxsize(525, 300)
        self.root.wm_iconbitmap('qr-code-scan.ico')

        # BG IMAGE
        img = Image.open('bg.jpg')
        img = img.resize((525, 300), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.bg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # LABEL for Entering website

        self.wb_lbl = Label(self.root, text='Enter URL', font=('sans serif', 20, 'bold'), bg='#000049', fg='white')
        self.wb_lbl.place(x=180, y=50)

        # Entry URL

        self.url_entry = ttk.Entry(self.root, font=('SANS SERIF', 15))
        self.url_entry.place(x=45, y=120, height=30, width=450)

        butt = Button(self.root, text='Get QR', font=('Sans serif', 15, 'bold'),
                             bg='#1F2F98', activebackground='#1F2F98', cursor='hand2', command=self.quick_response)
        butt.place(x=90, y=200, height=40, width=350)

    def quick_response(self):
        if self.url_entry.get() == "":
            messagebox.showerror('Error!', 'Please Fill the requirement details')
        else:
            self.new_window = Toplevel(self.root)
            self.app = Quick(self.new_window, self.url_entry.get())
            self.url_entry.delete(0, END)


if __name__ == '__main__':
    win = Tk()
    obj = QR(win)
    win.mainloop()

