from tkinter import *
from tkinter import messagebox
import sys

tampilan = Tk()
# judul = Label(tampilan,"Pasangan Calon Pemilihan Presiden 2019")
# judul.pack()
tombol1 = Button(tampilan, text="01")
tombol2 = Button(tampilan, text="02")
tombol1.pack(side=LEFT, padx=10)
tombol2.pack(side=RIGHT, padx=10)

def tampil01():
    print("Pasangan No Urut 01. Jokowi - Ma'ruf Amin")
    messagebox.showinfo("01","Pasangan No Urut 01. Jokowi - Ma'ruf Amin")
    #sys.exit(0)
	
def tampil02():
    print("Pasangan No Urut 02. Prabowo - Sandi")
    messagebox.showinfo("02","Pasangan No Urut 02. Prabowo - Sandiaga Uno")
    #sys.exit(0)
	
tombol1.configure(command=tampil01)
tombol2.configure(command=tampil02)

tampilan.mainloop()
