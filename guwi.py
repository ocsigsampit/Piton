from Tkinter import *

tampilan = Tk()
# judul = Label(tampilan,"Pasangan Calon Pemilihan Presiden 2019")
# judul.pack()
tombol1 = Button(tampilan, text="01")
tombol2 = Button(tampilan, text="02")
tombol1.pack(side=LEFT, padx=10)
tombol2.pack(side=RIGHT, padx=10)

def tampil01():
    print "Pasangan No Urut 01. Jokowi - Ma'ruf Amin"
	
def tampil02():
    print "Pasangan No Urut 02. Prabowo - Sandi"
	
tombol1.configure(command=tampil01)
tombol2.configure(command=tampil02)

tampilan.mainloop()