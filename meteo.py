#! /usr/bin/env python3
# weather info 

import json
from pprint import pprint
import urllib.request

## CIty List http://openweathermap.org/help/city_list.txt
source = 'http://api.openweathermap.org/data/2.5/forecast/city?id=2935517&APPID=846811144226bf0b31ecb2f14b307e9b&units=metric&lang=fr'

def main():

    print('En train d\'éffectuer la requête météo')
    table = urllib.request.urlopen(source)
    table_str = table.read().decode('utf-8')
    table_obj = json.loads(table_str)
    print("La méteo pour {0}\n".format(table_obj['city']['name']))
    print("Il fait entre {0} et {1} C°".format(table_obj['list'][0]['main']['temp_min'], table_obj['list'][0]['main']['temp_max']))
    print("On va appeller un chat un chat \n")
    print("Il fait {0}".format(table_obj['list'][0]['weather'][0]['description']))
if __name__ == '__main__':
    main()
