import xmlrpclib

print "Pilih perkiraan cuaca dibawah ini :"
print "1. Cuaca Indonesia"
print "2. Cuaca Dunia"
print "3. Cuaca Wisata"
print "4. Cuaca Jabodetabek"
print "5. Cuaca Harian Indonesia"
print "6. Exit"
pilih = raw_input("Pilihanmu : ").strip()

proxy = xmlrpclib.ServerProxy("http://localhost:8000")
if pilih=='1':
	feeds = proxy.getCuaca1()
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
	#print "Peringatan : %s" % feeds['peringatan']
		
if pilih=='2':
	feeds = proxy.getCuaca2()
	print "***Perkiraan Cuaca Dunia***"
	print "Tanggal : %s" % feeds['tgl']
	i = 0
	for feed in feeds['item']:
		print "Kota : %s" % feed['kota']
		print "Cuaca : %s" % feed['cuacaKota']
		print "Suhu Min : %s" % feed['suhumin']
		print "Suhu Max : %s" % feed['suhumax']
		print "---------------------------------"
		i+=1
	#print "Peringatan : %s" % feeds['peringatan']
	
if pilih=='3':
	feeds = proxy.getCuaca3()
	print "***Perkiraan Cuaca Wisata***"
	print "Tanggal Mulai: %s" % feeds['dateStart']
	print "Waktu Mulai: %s" % feeds['timeStart']
	print "Tanggal Sampai: %s" % feeds['dateEnd']
	print "Waktu Sampai: %s" % feeds['timeEnd']
	print "*****Lokasi*****"
	print "Cuaca Bali : %s" % feeds['baliWeather']
	print "Arah Angin : %s" % feeds['windDirect']
	print "Kecepatan Angin : %s" % feeds['windSpeed']
	print "Waktu Sunrise : %s" % feeds['sunrise']
	print "Waktu Sunset : %s" % feeds['sunset']
	print "****Daerah Bali****"
	i = 0
	for feed in feeds['item']:
		print "Wilayah : %s" % feed['area']
		print "Cuaca : %s" % feed['weather']
		#print "Simbol Cuaca : %s" % feed['weatherSym']
		print "Suhu : %s" % feed['temp']
		print "Kelembapan udara : %s" % feed['humidity']
		print "Ketinggian Gelombang : %s" % feed['wave']
		print "---------------------------------"
		i+=1

if pilih=='4':
	feeds = proxy.getCuaca4()
	print "***Perkiraan Cuaca Jabodetabek***"
	print "Tanggal : %s" % feeds['tgl']
	i = 0
	for feed in feeds['item']:
		print "Daerah : %s" % feed['daerah']
		print "Cuaca Pagi : %s" % feed['pagi']
		print "Cuaca Siang : %s" % feed['siang']
		print "Cuaca Malam : %s" % feed['malam']
		print "---------------------------------"
		i+=1

if pilih=='5':
	feeds = proxy.getCuaca5()
	print "***Perkiraan Cuaca Harian Indonesia***"
	print "Update : %s" % feeds['update']
	print "Jam Update : %s" % feeds['jamupdate']
	i = 0
	for feed in feeds['item']:
		print "Valid : %s" % feed['valid']
		print "Cuaca : %s" % feed['weather']
		print "Arah Angin : %s" % feed['winddirection']
		print "Kecepatan Angin : %s" % feed['windspeed']
		print "Suhu : %s" % feed['temperature']
		print "Kelembapan : %s" % feed['humidity']
		print "Waktu Sunrise : %s" % feed['sunrise']
		print "Waktu Sunset : %s" % feed['sunset']
		print "Waktu Moonrise : %s" % feed['moonrise']
		print "Waktu Moonset : %s" % feed['moonset']
		print "Tinggi Gelombang Utara : %s" % feed['waveheightnortcoast']
		print "Tinggi Gelombang Selatan : %s" % feed['waveheightsouthcoast']
		print "---------------------------------"
		i+=1
