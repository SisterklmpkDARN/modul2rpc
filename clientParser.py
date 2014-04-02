import xmlrpclib



print "Pilih perkiraan cuaca dibawah ini :"
print "1. Cuaca Dunia1"
print "2. Cuaca Indonesia1"
print "3. Cuaca Jabodetabek1"
print "4. Cuaca Harian"
print "5. Cuaca Wisata"
print "6. Exit"
pilih = raw_input("Pilihanmu : ").strip()
#print "Pilihanmu : %s" % (pilih)

proxy = xmlrpclib.ServerProxy("http://localhost:8000")
feeds = proxy.getCuaca1()
if pilih=='1':
	print "***Perkiraan Cuaca Indonesia***"
	print "Tanggal Mulai : %s" % feeds['mulai']
	print "Tanggal Sampai : %s" % feeds['sampai']
	i = 0
	for feed in feeds['item']:
		print "Kota : %s" % feed['kota']
		print "Cuaca : %s" % feed['cuacaKota']
		print "Suhu Min : %s" % feed['suhumin']
		print "Suhu Max : %s" % feed['suhumax']
		print "Kelembapan Min : %s" % feed['kelMin']
		print "Kelembapan Max : %s" % feed['kelMax']
		print "---------------------------------"
		i+=1
		
if pilih=='2':
	print proxy.coba()
