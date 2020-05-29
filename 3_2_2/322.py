import xmltodict
import collections

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

cnt1 = 0
cnt2 = 0

parsedxml = xmltodict.parse(xml)
for node in parsedxml['osm']['node']:
    if 'tag' in node:
        cnt1 += 1
    else:
        cnt2 += 1

print(cnt1, cnt2)
