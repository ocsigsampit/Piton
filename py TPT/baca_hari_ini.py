#update per 05/02/2018 08:00 PC TPT
#memperbaiki nama nomor BPS

import PyPDF2, os


pdfFiles = []
cari_tgl_bps3 = ""

for filename in os.listdir('.'):
	# if filename.endswith('.pdf') and filename.startswith('Py'):
	if filename.endswith('.pdf') and filename.startswith('BP'):
		pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
#print pdfFiles

#for x in pdfFiles:
#	print ">" + x + "<"

for filename2 in pdfFiles:
	pdfFileObj = open(filename2, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(0)
	teks = pageObj.extractText()
	
	#======================================#
	#split dengan spasi untuk mencari no bps
	#======================================#	
	cari_no_bps = teks.split(" ")
	
	no_bps = cari_no_bps[1]
	no_bps = no_bps[9:50]
	no_bps = no_bps.strip()
	no_bps = no_bps.split("/")
	no_bps = no_bps[0]+ "/" + no_bps[1] + "/" + no_bps[2]+ "/" + (no_bps[3])[0:4]
	
	#print ">" + no_bps + "<"
	
	#==============================================================#
	#split dengan "Tgl. Diterima :" untuk mencari tanggal terima bps
	#==============================================================#
	cari_tgl_bps = teks.split("Tgl. Diterima :")
	cari_tgl_bps = cari_tgl_bps[1]
	cari_tgl_bps = cari_tgl_bps[0:11].strip()
	#print cari_tgl_bps[1:2]
	cari_tgl_bps2 = cari_tgl_bps[1:2]
	if cari_tgl_bps2 == "-":
		tgl_bps = "0" + cari_tgl_bps
		tgl_bps = tgl_bps[0:10]
	else:
		tgl_bps = cari_tgl_bps
	
	#print cari_tgl_bps,"- ",tgl_bps
	#print ">" + tgl_bps + "<"
	tgl_saja = tgl_bps.split("-")[0]
	
	#================================================================#
	#split dengan "NAMA LENGKAPNIPPANJANG" untuk mencari jenis layanan
	#================================================================#
	cari_layanan = teks.split("BUDIONO198308142002121003")
	layanan = cari_layanan[0].split(',')
	layanan = layanan[-1]
	
	#print ">" + layanan + "<" 
		
	#print filename2, "|", no_bps, "|",layanan, "|" ,tgl_bps, "||"
	tulisan = filename2 + "_" + no_bps + "_" + layanan + "_" + tgl_bps + "_" + "_" + tgl_saja + "\n"
	print tulisan
	#tulisan = tulisan.encode('ascii', 'ignore')
	#tulisan = layanan.strip()
	#berkas.write(tulisan)
	