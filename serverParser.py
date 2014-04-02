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
				#print "Kota : %s" % kota.childNodes[0].data
				cuacaKota = row.getElementsByTagName('Cuaca')[0]
				dataItem['cuacaKota'] = cuacaKota.childNodes[0].data
				#print "Cuaca : %s" % cuacaKota.childNodes[0].data
				suhumin = row.getElementsByTagName('SuhuMin')[0]
				dataItem['suhumin'] = suhumin.childNodes[0].data
				#print "Suhu Minimum : %s" % suhumin.childNodes[0].data
				suhumax = row.getElementsByTagName('SuhuMax')[0]
				dataItem['suhumax'] = suhumax.childNodes[0].data
				#print "Suhu Maksimum : %s" % suhumax.childNodes[0].data
				kelMin = row.getElementsByTagName('KelembapanMin')[0]
				dataItem['kelMin'] = kelMin.childNodes[0].data
				#print "Kelembapan Minimum : %s" % kelMin.childNodes[0].data
				kelMax = row.getElementsByTagName("KelembapanMax")[0]
				dataItem['kelMax'] = kelMax.childNodes[0].data
				#print "Kelembapan Maksimum : %s" % kelMax.childNodes[0].data
				collections.append(dataItem)
				i+=1
				xml['item'] = collections
	return xml	
def coba():
	x = 1 + 2
	return x
	
server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on  port 8000.."
#server.register_inrospection_functions()
server.register_multicall_functions()
server.register_function(getCuaca1, 'getCuaca1')
server.register_function(coba, 'coba')
server.serve_forever()
#print data
#------------------------------------------------------------------------

