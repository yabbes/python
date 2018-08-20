#! /usr/bin/env python3

import os
import xml.etree.ElementTree as ET
from shutil import copyfile
zielpfad = '/home/tschw/code/kameradateien/ziel/'
quelle = ''

stunden = [x[0] for x in os.walk('.')]
for stunde in stunden:
    aufnahmen = [x[0] for x in os.walk(stunde)]
    for aufnahme in aufnahmen:
        pfadaufnahme = os.path.abspath(aufnahme)
        pfadxml = os.path.dirname(aufnahme) + '/recording.xml'
        if os.path.exists(pfadxml):
            print(pfadxml)
            xmlrealpath = os.path.realpath(pfadxml)
            tree = ET.parse(xmlrealpath)
            root = tree.getroot()
            for sosse in root.iter('SourceToken'):
                quelle = sosse.text
            print("Source = {}".format(quelle))
            for wurzel, dirs, files in os.walk(aufnahme):
                for vid in files:
                    if vid.endswith('.mkv'):
                        print(pfadaufnahme + '/' + os.path.normpath(vid))
                        vidpfad = pfadaufnahme + '/' + os.path.normpath(vid)
                        #print(zielpfad + quelle + '/' + vid)
                        copyfile(vidpfad, zielpfad + quelle + '/' + vid)


        #tree = ET.parse(pfad + '/recording.xml')
        #root = tree.getroot()
"""  
    for name in files:
        if name.endswith('recording.xml'):
            print(name)
            tree = ET.parse(name)
            root = tree.getroot()
            for sosse in root.iter('Source'):
                quelle = sosse.text
                print("Source = {}".format(quelle))
        #if name.endswith('.mkv'):
        #    print('video mit source {}'.format(quelle))
        #print(dirs)
"""