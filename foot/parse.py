#! /usr/bin/env python3
# parsing json data bundesliga table

import json
from pprint import pprint

def main():
    print("Opening json sample")
    with open('buli.json') as teams_data:
        teams = json.load(teams_data)
    # pprint(data)
    for team in teams['standing']:
        print(team['teamName'])
if __name__ == '__main__':
    main()
