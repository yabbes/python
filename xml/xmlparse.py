import xml.etree.ElementTree
import os

directory = '.'

t_list = []

for filename in os.listdir(directory):
	if filename.endswith(".xml"):
		e = xml.etree.ElementTree.parse(filename).getroot()
		print(filename)
		#e.findall('./TReference').attrib['Name']
		for elem in e.iter('TReference'):
			name = elem.attrib.get('Name')
			#print(name)
			if name in t_list:
				continue
			else:
				t_list.append(name)
				
print(t_list)
