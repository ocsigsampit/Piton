import PyPDF2
import re

bukaBerkas = open('registere2.pdf','rb')
bacaBerkas = PyPDF2.PdfFileReader(bukaBerkas)
bacaHalamanSatu = bacaBerkas.getPage(0)
hasilBaca = bacaHalamanSatu.extractText()
	
print(hasilBaca)

tgl_register = hasilBaca.split("SPT")
tgl_register = tgl_register[0]
tgl_register = tgl_register.split(" : ")
tgl_register = tgl_register[1]
tgl_register = tgl_register.strip()

npwps = re.findall(r'\d{2}\.\d{3}\.\d{3}\.\d{1}\-\d{3}\.\d{3}',hasilBaca)
bpss  = re.findall(r'S\-\d+\/\w+\/\w+\.\d+\/\w+\.\d+\/\d{4}',hasilBaca)
noregs  = re.findall(r'REG\-\d+\/\w+\/\w+\.\d+\/\w+\.\d+\/\d{4}',hasilBaca)
namawps  = re.findall(r'\w{1}\d+[\w+\s]*\d{2}\.\d{3}\.\d{3}',hasilBaca)

for noreg in noregs:
	print("No Register : ",noreg," Tanggal Register : ",tgl_register)
	
for namawp in namawps:
	print("Nama WP : ",namawp)

'''
kamus = dict(zip(bpss, npwps))

for x,y in kamus.items():
print("INSERT INTO tb_register_tpt VALUES (tgl_register,npwp,bps) VALUES ('",tgl_register,"','",x,"','",y,"')")
'''