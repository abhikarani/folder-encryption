username = 'root'
password = 'root'
inputuser = input('[*] Enter username: ')
inputpass = input('[*] Enter password: ')
if not (username==inputuser and password==inputpass):
    print('Incorrect username or password!\nPlease try again.')
    exit()

import pyAesCrypt
import glob
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from tkinter import *
import getpass
import sys

# encrypted_folder = ['']

def encryptThis(directory, password):
    global encrypted_folder
    # lambda: print("button_1 clicked")
    # Encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    # Get current directory
    curDir = ''
    # Prompt user for password to encrypt files
    # password1 = input('\n> Enter password to encrypt: ')
    print(directory)
    # encrypted_folder = encrypted_folder.append(directory)
    print('\n> Beginning recursive encryption...\n\n')
    # Main loop to encrypt all files recursively
    for x in glob.glob(f'{directory}\\**\*', recursive=True):
        print("1")
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, x + '.aes')
        # Encrypt
        if os.path.isfile(fullpath):
            print('>>> Original: \t' + fullpath + '')
            print('>>> Encrypted: \t' + fullnewf + '\n')
            pyAesCrypt.encryptFile(fullpath, fullnewf, password, bufferSize)
            # Remove file after encryption
            os.remove(fullpath)
    print("Encryption complete: ")



def decryptThis(directory, password):
    lambda: print("button_2 clicked")
    # Encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    # Get current directory
    curDir = os.getcwd()
    # Prompt user for password to decrypt files
    # password1 = input('\n> Enter password to decrypt: ')
    
    print('\n> Beginning recursive decryption...\n\n')
    # Main loop to decrypt all files recursively
    for x in glob.glob(f'{directory}\\**\*', recursive=True):
        fullpath = os.path.join(curDir, x)
        fullnewf = os.path.join(curDir, os.path.splitext(x)[0])
        # Decrypt
        if os.path.isfile(fullpath):
            print('>>> Encrypted: \t' + fullpath + '')
            try:
                pyAesCrypt.decryptFile(fullpath, fullnewf, password, bufferSize)
                print('>>> Decrypted: \t' + fullnewf + '\n')
                os.remove(fullpath)     # Remove encrypted file after decrypt
            except ValueError:
                print('>>> Error - Wrong password!\n')
    print("Decryption complete")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\abhi\aaa VIT LECTURES\semm 6\CSE3502 ISM\project\code_execution\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("640x417")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 817,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(#background rectangle
    0.0,
    0.0,
    1440.0,
    817.0,
    fill="#0C0220",
    outline="")

canvas.create_rectangle(#navbar rectangle
    0.0,
    26.99999999999997,
    1440.0,
    97.99999999999997,
    fill="#764343",
    outline="")

canvas.create_text(#navbar text
    70.0,
    51.99999999999997,
    anchor="nw",
    text="CryptoLocker",
    fill="#000000",
    font=("IstokWeb Bold", 18 * -1)
)

canvas.create_text(
    95.0,
    124.0,
    anchor="nw",
    text="Browse the file you want to encrypt ",
    fill="#FFFFFF",
    font=("IstokWeb Bold", 22 * -1)
)

canvas.create_text(
    95.0,
    295.0,
    anchor="nw",
    text="Browse the file you want to decrypt ",
    fill="#FFFFFF",
    font=("IstokWeb Bold", 22 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("lock.png"))

button_1 = Button(
    image=button_image_1,
    bg="#0C0220",
    borderwidth=1,
    highlightthickness=0,
    relief="flat",
    command=lambda: encryptThis(filedialog.askdirectory(),getpass.getpass("Enter the password to encrypt: "))
)
button_1.place(
    x=536.0,
    y=119.0,
    width=43.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("unlock.png"))

button_2 = Button(
    image=button_image_2,
    bg="#0C0220",
    borderwidth=1,
    highlightthickness=0,
    relief="flat",
    command=lambda: decryptThis(filedialog.askdirectory(),getpass.getpass("Enter the password to decrypt: "))
)
button_2.place(
    x=536.0,
    y=289.0,
    width=43.0,
    height=43.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    688.0,
    282.0,
    image=image_image_1
)
window.resizable(True, True)
window.mainloop()

# print(encrypted_folder)
# for x in encrypted_folder:
#     print(x)
#     rc = os.system("handle.exe -accepteula %s | findstr pid" %(x))
#     if 0 == rc:
#         decryptThis(x,getpass.getpass("Enter the password to decrypt: "))
#     else:
#         print('No process open this folder now.')