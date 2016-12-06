#! /usr/bin/env python3
# parsing json data bundesliga table

import json
from pprint import pprint
import urllib.request

## load json object of current league table from url
table = urllib.request.urlopen('http://api.football-data.org/v1/soccerseasons/430/leagueTable')
table_str = table.read().decode('utf-8')
table_obj = json.loads(table_str)


def main():
    print("Opening current league table matchday {0}".format(table_obj['matchday']))
    # pprint(data)
    for team in table_obj['standing']:
        ##print(len(team['teamName']))
        if len(team['teamName']) <= 14:
            print('{0})\t {1}\t\t\t {2} Pkt\t {3} Tore'.format(team['position'], team['teamName'],
            team['points'], team['goals']))
        else:
            print('{0})\t {1}\t\t {2} Pkt\t {3} Tore'.format(team['position'], team['teamName'],
            team['points'], team['goals']))


if __name__ == '__main__':
    main()
