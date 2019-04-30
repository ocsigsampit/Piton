import PyPDF2
import re
import mysql.connector as mariadb
import os

db = mariadb.connect(user="root", password="", database="test")
cursor = db.cursor()

cursor.execute("TRUNCATE TABLE registerspt")
db.commit()

berkasRegister = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf') and filename.startswith('REG-'):
		berkasRegister.append(filename)
		
berkasRegister.sort(key=str.lower)

for berkas in berkasRegister:
	bukaBerkas = open(berkas,'rb')
	bacaBerkas = PyPDF2.PdfFileReader(bukaBerkas)
	bacaHalamanSatu = bacaBerkas.getPage(0)
	hasilBaca = bacaHalamanSatu.extractText()
	
	tgl_register = hasilBaca.split("SPT")
	tgl_register = tgl_register[0]
	tgl_register = tgl_register.split(" : ")
	tgl_register = tgl_register[1]
	tgl_register = tgl_register.strip()

	npwps = re.findall(r'\d{2}\.\d{3}\.\d{3}\.\d{1}\-\d{3}\.\d{3}',hasilBaca)
	bpss  = re.findall(r'S\-\d+\/\w+\/\w+\.\d+\/\w+\.\d+\/\d{4}',hasilBaca)
	
	kamus = dict(zip(bpss, npwps))

	for x,y in kamus.items():
		print("INSERT INTO tb_register_tpt VALUES (tgl_register,npwp,bps) VALUES ('",tgl_register,"','",x,"','",y,"')")
		cursor.execute("INSERT INTO registerspt (tgl_register,npwp,bps) VALUES ('" + tgl_register + "','" + x + "','" + y + "')")
		db.commit()