import PyPDF2
import re
import sys
import pymysql
import mysql.connector
import os
from time import sleep

db = pymysql.connect(db="pengemasan", user="root", passwd="", host="127.0.0.1", port=3306)

cursor = db.cursor()

cursor.execute("TRUNCATE TABLE tb_register_spt")
db.commit()

berkasRegister = []

jumlahBPS = 0

for filename in os.listdir('.'):
	if filename.endswith('.pdf') and filename.startswith('REG-'):
		berkasRegister.append(filename)
		
berkasRegister.sort(key=str.lower)

for berkas in berkasRegister:
	bukaBerkas = open(berkas,'rb')
	bacaBerkas = PyPDF2.PdfFileReader(bukaBerkas)
	jumlahHalaman = bacaBerkas.getNumPages()
	
	for halaman in range(jumlahHalaman):
		bacaHalaman = bacaBerkas.getPage(halaman)
		hasilBaca = bacaHalaman.extractText()
		
		if halaman == 0:
			noregs  = re.findall(r'REG\-\d+\/\w+\/\w+\.\d+\/\w+\.\d+\/\d{4}',hasilBaca)
			noregs  = noregs[0]
			noregs  = str(noregs)

			tgl_register = hasilBaca.split("SPT")
			tgl_register = tgl_register[0]
			tgl_register = tgl_register.split(" : ")
			tgl_register = tgl_register[1]
			tgl_register = tgl_register.strip()

		npwps = re.findall(r'\d{2}\.\d{3}\.\d{3}\.\d{1}\-\d{3}\.\d{3}',hasilBaca)
		bpss  = re.findall(r'S\-\d+\/\w+\/\w+\.\d+\/\w+\.\d+\/\d{4}',hasilBaca)
	
		kamus = dict(zip(bpss, npwps))
		
	for x,y in kamus.items():
		cursor.execute("INSERT INTO tb_register_spt (no_reg,tgl_str_reg,no_bps,npwp) VALUES ('" + noregs + "','" + tgl_register + "','" + x + "','" + y + "')")
		db.commit()
		#print("Halaman : ",halaman,"\n")
		barisPertama = "Nomor Register : " + str(noregs) + " Tgl Register : " + str(tgl_register) + " No BPS : " + str(x) + " NPWP : " + (y) + "\n"
		strBarisPertama = str(barisPertama)
		strBarisPertama = strBarisPertama + "\n"
		#print("Str barisPertama : " + strBarisPertama)
		sys.stdout.write(strBarisPertama)
		
		jumlahBPS = jumlahBPS + 1
		strJumlahBPS = str(jumlahBPS)
		strJumlahBPS = "Jumlah BPS : " + strJumlahBPS + "\n"
		#print(strJumlahBPS)
		sys.stdout.write(strJumlahBPS)
		
		sys.stdout.flush()