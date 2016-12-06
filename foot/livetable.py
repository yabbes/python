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
        print('{0}) {1}'.format(team['position'], team['teamName']))

if __name__ == '__main__':
    main()
