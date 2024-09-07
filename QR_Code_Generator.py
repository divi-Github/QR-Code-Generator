'''
                            [QR Code Generator {QCG}]
                        Programming language used --> Python  
'''

# Importing Modules
import pyqrcode
import png
from pyqrcode import QRCode

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox


# Creating necessary functions
def create_qr():
    l = user_input.get()
    if l:
        qr = pyqrcode.create(l)
        qr.png("QR.png", scale = 6)
        show_qr()
    else:
        messagebox.showwarning("!! WARNING !!", "Please Enter a Link/URL for QR Code Generation")

def show_qr():
    img = Image.open("QR.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

def save_qr():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        qr_image = Image.open("QR.png")
        qr_image.save(filename)

# Main Window (using tkinter)
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("600x500")  
root.resizable(False, False)

# creates label widgets with a text
input_label = tk.Label(root, text="!! QR Code Generator !!")
input_label.pack(padx=30, pady=30)

input_label = tk.Label(root, text="Enter Link/URL: ")
input_label.pack(padx=30, pady=10)

# Creates a string variable to store the user’s input (link or URL).
user_input = tk.StringVar()

# Creates an input field (text box) where the user can type their link.
entry = tk.Entry(root, textvariable=user_input,font=("Arial",14))
entry.pack(padx=30, pady=10)

# Generating QR Code Button (Button Widget):
generate_button = tk.Button(root, text="Generate QR Code", command=create_qr)
generate_button.pack()

# QR Code Display Area (Label Widget):
qr_label = tk.Label(root)
qr_label.pack()

# Generating Save QR Code Button (Button Widget):
save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack()

# Running the Tkinter Event Loop
root.mainloop()

'''********************END OF THE CODE********************'''