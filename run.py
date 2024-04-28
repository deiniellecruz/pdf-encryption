from Crypto.Cipher import ARC4
import tkinter as tk
from tkinter import filedialog
import getpass


def selectfile():
    while True:
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        filename = filedialog.askopenfilename(filetypes= [('PDF Files', '*.pdf')])
        root.quit()
        if len(filename) == 0:
            print('a')
        else:
            #file_path = os.path.dirname(filename)
            #file_relpath=os.path.relpath(filename)
            return filename


def key_input():
    key = getpass.getpass("Enter key: ") 
    key = key.encode()
    return key
    

def encrypt_pdf(key):

    filename = selectfile()
    file = open(filename, 'rb') 
    pdf_data = file.read()
    file.close()

    cipher = ARC4.new(key)
    encrypted_data = cipher.encrypt(pdf_data)

    enc_file = open(filename,'wb')
    enc_file.write(encrypted_data)
    enc_file.close()
    print("PDF encrypted and saved successfully.")


def decrypt_pdf(key):
    filename = selectfile()
    file = open(filename, 'rb')
    encrypted_pdf_data = file.read()
    file.close()

    cipher = ARC4.new(key)
    decrypted_pdf_data = cipher.decrypt(encrypted_pdf_data)

    dec_file = open(filename, 'wb') 
    dec_file.write(decrypted_pdf_data)
    dec_file.close()

    print("PDF decrypted and saved successfully.")
    



while True:
    
    print("-" * 50)
    print(" PDF Encryption")
    print(" Encryption(1)")
    print(" Decryption(2)")
    print(" Exit(3)")
    choice = int(input(" Choose what to do: "))
    print("-" * 50)


    if choice == 3:
        print("nagexit ka man e!")
        break

    elif choice == 1:
        key = key_input()
        encrypt_pdf(key)

    elif choice == 2:
        key = key_input()
        decrypt_pdf(key)

    
    