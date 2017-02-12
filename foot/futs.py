#! /usr/bin/env python3
# parsing json data bundesliga table

import json
import urllib.request


# load json object of current league table from url
en_source = 'http://api.football-data.org/v1/soccerseasons/426/leagueTable'
de_source = 'http://api.football-data.org/v1/soccerseasons/430/leagueTable'
it_source = 'http://api.football-data.org/v1/soccerseasons/438/leagueTable'
es_source = 'http://api.football-data.org/v1/soccerseasons/436/leagueTable'
fr_source = 'http://api.football-data.org/v1/soccerseasons/434/leagueTable'


def main():
    print('Willkommen bei Futs dem Fußball-Tsentrum\n')
    print('Folgende Tabellen stehen zur Auswahl: \n\n'
          'en\t -> Premiere League\n'
          'de\t -> Bundesliga\n'
          'it\t -> Serie A\n'
          'es\t -> Primera División\n'
          'fr\t -> Ligue 1\n')
    eingabe = input()
    select = ''
    if eingabe == 'en':
        select = en_source
    elif eingabe == 'de':
        select = de_source
    elif eingabe == 'it':
        select = it_source
    elif eingabe == 'es':
        select = es_source
    elif eingabe == 'fr':
        select = fr_source

    table = urllib.request.urlopen(select)
    table_str = table.read().decode('utf-8')
    table_obj = json.loads(table_str)
    print("Aktueller Tabellenstand wird geöffnet; Spieltag {0}".
          format(table_obj['matchday']))
    for team in table_obj['standing']:
        if len(team['teamName']) <= 14:
            print('{0})\t {1}\t\t\t {2} Sp\t {3} Pkt\t {4} Tore'.
                  format(team['position'], team['teamName'],
                         team['playedGames'], team['points'], team['goals']))
        elif len(team['teamName']) >= 23:
            print('{0})\t {1}\t {2} Sp\t {3} Pkt\t {4} Tore'.
                  format(team['position'], team['teamName'],
                         team['playedGames'], team['points'], team['goals']))
        else:
            print('{0})\t {1}\t\t {2} Sp\t {3} Pkt\t {4} Tore'.
                  format(team['position'], team['teamName'],
                         team['playedGames'], team['points'], team['goals']))


if __name__ == '__main__':
    main()
