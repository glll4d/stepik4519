<<<<<<< HEAD
import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
=======
import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
>>>>>>> f0ea5dec45d4d026e7666704cdec5baa45a4da47
print(parsedxml['osm']['node'][100]['@id'])