import urllib2
from xml.dom.minidom import parseString
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib


#------------------------------------------------------------------
def getCuaca1():
	file1 = urllib2.urlopen('http://data.bmkg.go.id/cuaca_indo_1.xml')
	data1 = file1.read()
	file1.close()

	dom1 = parseString(data1)

	cuaca = dom1.documentElement
	#get all Tanggal
	tanggals = cuaca.getElementsByTagName("Tanggal")
	#print detil tanggal
	xml = {}
	#def getCuaca():
	for tanggal in tanggals:		
		print "****Tanggal****"
		mulai = tanggal.getElementsByTagName('Mulai')[0]
		print "Mulai = %s" % mulai.childNodes[0].data
		xml['mulai'] = mulai.childNodes[0].data
		sampai = tanggal.getElementsByTagName('Sampai')[0]
		print "Sampai = %s" % sampai.childNodes[0].data
		xml['sampai'] = sampai.childNodes[0].data
				
		isis = cuaca.getElementsByTagName("Isi")
			
		for isi in isis:
			rows = isi.getElementsByTagName("Row")	
			collections = []
			i = 0
			for row in rows[:]:
				dataItem = {}
				print "-------------------"
				kota = row.getElementsByTagName('Kota')[0]
				dataItem['kota'] = kota.childNodes[0].data
				cuacaKota = row.getElementsByTagName('Cuaca')[0]
				dataItem['cuacaKota'] = cuacaKota.childNodes[0].data
				suhumin = row.getElementsByTagName('SuhuMin')[0]
				dataItem['suhumin'] = suhumin.childNodes[0].data
				suhumax = row.getElementsByTagName('SuhuMax')[0]
				dataItem['suhumax'] = suhumax.childNodes[0].data
				kelMin = row.getElementsByTagName('KelembapanMin')[0]
				dataItem['kelMin'] = kelMin.childNodes[0].data
				kelMax = row.getElementsByTagName("KelembapanMax")[0]
				dataItem['kelMax'] = kelMax.childNodes[0].data
				collections.append(dataItem)
				i+=1
				xml['item'] = collections
				
			#peringatan = isi.getElementsByTagName("Peringatan")
			#xml['peringatan'] = peringatan.childNodes[0].data
	return xml	
	
def getCuaca2():
	file1 = urllib2.urlopen('http://data.bmkg.go.id/cuaca_dunia_1.xml')
	data1 = file1.read()
	file1.close()

	dom1 = parseString(data1)

	cuaca = dom1.documentElement
	
	xml = {}
	
	#get all Tanggal
	tanggal = cuaca.getElementsByTagName("Tanggal")[0]
	xml['tgl'] = tanggal.childNodes[0].data
	#print detil tanggal
		
	isis = cuaca.getElementsByTagName("Isi")
			
	for isi in isis:
		rows = isi.getElementsByTagName("Row")
		collections = []
		i = 0
		for row in rows[:]:
			dataItem = {}
			print "-------------------"
			kota = row.getElementsByTagName('Kota')[0]
			dataItem['kota'] = kota.childNodes[0].data
			cuacaKota = row.getElementsByTagName('Cuaca')[0]
			dataItem['cuacaKota'] = cuacaKota.childNodes[0].data
			suhumin = row.getElementsByTagName('SuhuMin')[0]
			dataItem['suhumin'] = suhumin.childNodes[0].data
			#print "Suhu Minimum : %s" % suhumin.childNodes[0].data
			suhumax = row.getElementsByTagName('SuhuMax')[0]
			dataItem['suhumax'] = suhumax.childNodes[0].data
			collections.append(dataItem)
			i+=1
			xml['item'] = collections
			
		#peringatan = isi.getElementsByTagName("Peringatan")
		#xml['peringatan'] = peringatan.childNodes[0].data
	return xml	
	
def getCuaca3():
	file1 = urllib2.urlopen('http://data.bmkg.go.id/cuaca_wisata.xml')
	data1 = file1.read()
	file1.close()

	dom1 = parseString(data1)

	travelWeather = dom1.documentElement
	
	xml = {}
	
	#get all Tanggal
	date = travelWeather.getElementsByTagName("Date")[0]
	#for tgl in dates:
	valStart = date.getElementsByTagName("ValidStart")[0]
	xml['dateStart'] = valStart.childNodes[0].data
	valTime= date.getElementsByTagName("ValidTimeStart")[0]
	xml['timeStart'] = valTime.childNodes[0].data
	valEnd = date.getElementsByTagName("ValidEnd")[0]
	xml['dateEnd'] = valEnd.childNodes[0].data
	valTimeEnd = date.getElementsByTagName("ValidTimeEnd")[0]
	xml['timeEnd'] = valTimeEnd.childNodes[0].data
	#print detil tanggal
		
	forecasts = travelWeather.getElementsByTagName("Forecast")
			
	for forecast in forecasts:
		generals = forecast.getElementsByTagName("General")
		for general in generals:
			baliWeather = general.getElementsByTagName("BaliWeather")[0]
			xml['baliWeather'] = baliWeather.childNodes[0].data
			windDirect= general.getElementsByTagName("WindDirection")[0]
			xml['windDirect'] = windDirect.childNodes[0].data
			windSpeed = general.getElementsByTagName("WindSpeed")[0]
			xml['windSpeed'] = windSpeed.childNodes[0].data
			sunrise = general.getElementsByTagName("Sunrise")[0]
			xml['sunrise'] = sunrise.childNodes[0].data
			sunset = general.getElementsByTagName("Sunset")[0]
			xml['sunset'] = sunset.childNodes[0].data
				
		rows = forecast.getElementsByTagName("Row")
		collections = []
		i = 0
		for row in rows[:]:
			dataItem = {}
			print "-------------------"
			area = row.getElementsByTagName('Area')[0]
			dataItem['area'] = area.childNodes[0].data
			weather = row.getElementsByTagName('Weather')[0]
			dataItem['weather'] = weather.childNodes[0].data
			weatherSym = row.getElementsByTagName('WeatherSymbol')[0]
			dataItem['weatherSym'] = weatherSym.childNodes[0].data
			temp = row.getElementsByTagName('Temperature')[0]
			dataItem['temp'] = temp.childNodes[0].data
			humidity = row.getElementsByTagName('Humidity')[0]
			dataItem['humidity'] = humidity.childNodes[0].data
			wave = row.getElementsByTagName('WaveHeight')[0]
			dataItem['wave'] = wave.childNodes[0].data
			collections.append(dataItem)
			i+=1
			xml['item'] = collections
			
	return xml	
	
def getCuaca4():
	file1 = urllib2.urlopen('http://data.bmkg.go.id/cuaca_jabodetabek_1.xml')
	data1 = file1.read()
	file1.close()

	dom1 = parseString(data1)

	cuaca = dom1.documentElement
	
	xml = {}
	
	#get all Tanggal
	tanggal = cuaca.getElementsByTagName("Tanggal")[0]
	xml['tgl'] = tanggal.childNodes[0].data
	#print detil tanggal
		
	isis = cuaca.getElementsByTagName("Isi")
	for isi in isis:
		rows = isi.getElementsByTagName("Row")
		collections = []
		i = 0
		for row in rows[:]:
			dataItem = {}
			print "-------------------"
			daerah = row.getElementsByTagName('Daerah')[0]
			dataItem['daerah'] = daerah.childNodes[0].data
			pagi = row.getElementsByTagName('Pagi')[0]
			dataItem['pagi'] = pagi.childNodes[0].data
			siang = row.getElementsByTagName('Siang')[0]
			dataItem['siang'] = siang.childNodes[0].data
			malam = row.getElementsByTagName('Malam')[0]
			dataItem['malam'] = malam.childNodes[0].data
			collections.append(dataItem)
			i+=1
			xml['item'] = collections
			
		#peringatan = isi.getElementsByTagName("Peringatan")
		#xml['peringatan'] = peringatan.childNodes[0].data
	return xml	
	
server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on  port 8000.."
#server.register_inrospection_functions()
server.register_multicall_functions()
server.register_function(getCuaca1, 'getCuaca1')
server.register_function(getCuaca2, 'getCuaca2')
server.register_function(getCuaca3, 'getCuaca3')
server.register_function(getCuaca4, 'getCuaca4')
server.serve_forever()
#print data
#------------------------------------------------------------------------

